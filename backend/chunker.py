import re

# Files that strongly indicate technical debt when present
DEBT_SIGNAL_PATTERNS = [
    r'TODO', r'FIXME', r'HACK', r'XXX', r'TEMP', r'DEPRECATED',
    r'console\.log', r'print\(', r'debugger', r'breakpoint',
    r'password\s*=', r'secret\s*=', r'api_key\s*=', r'token\s*=',
    r'hardcoded', r'workaround', r'quick.?fix', r'tech.?debt'
]

# Debt category hints per file/path pattern
DEBT_CATEGORY_HINTS = {
    'test': 'testing',
    'spec': 'testing',
    '__tests__': 'testing',
    'mock': 'testing',
    'package.json': 'dependencies',
    'requirements.txt': 'dependencies',
    'pom.xml': 'dependencies',
    'go.mod': 'dependencies',
    'dockerfile': 'architecture',
    'docker-compose': 'architecture',
    '.github/workflows': 'architecture',
    'config': 'architecture',
    'router': 'architecture',
    'route': 'architecture',
    'controller': 'architecture',
    'model': 'architecture',
    'service': 'architecture',
    'util': 'code_quality',
    'helper': 'code_quality',
    'common': 'code_quality',
    'shared': 'code_quality',
    'legacy': 'code_quality',
    'old': 'code_quality',
    'deprecated': 'code_quality',
}

EXT_MAP = {
    "py": "python", "js": "javascript", "ts": "typescript",
    "jsx": "javascript", "tsx": "typescript", "java": "java",
    "go": "go", "rb": "ruby", "php": "php", "c": "c",
    "cpp": "cpp", "cs": "csharp", "md": "markdown", "json": "json",
    "yml": "yaml", "yaml": "yaml", "html": "html", "css": "css"
}


def get_debt_category_hint(file_path):
    """Infer which debt category a file most likely relates to."""
    path_lower = file_path.lower()
    for pattern, category in DEBT_CATEGORY_HINTS.items():
        if pattern in path_lower:
            return category
    return 'code_quality'


def scan_debt_signals(content):
    """
    Scan raw file content for known debt signal patterns.
    Returns a list of {pattern, line_number, line_snippet} matches
    so analysis has exact line-level evidence.
    """
    signals = []
    lines = content.splitlines()
    for line_num, line in enumerate(lines, start=1):
        for pattern in DEBT_SIGNAL_PATTERNS:
            if re.search(pattern, line, re.IGNORECASE):
                signals.append({
                    "pattern": pattern,
                    "line_number": line_num,
                    "line_snippet": line.strip()[:120]
                })
                break
    return signals


def compute_file_metrics(content, language):
    """
    Lightweight static metrics computed for each file.
    These give Bedrock hard numbers to ground its analysis.
    """
    lines = content.splitlines()
    total_lines = len(lines)
    blank_lines = sum(1 for l in lines if not l.strip())
    comment_lines = 0
    long_functions = []
    max_indent = 0

    # Language-specific comment detection
    comment_prefixes = {
        'python': ('#',),
        'javascript': ('//', '/*', '*'),
        'typescript': ('//', '/*', '*'),
        'java': ('//', '/*', '*'),
        'go': ('//',),
        'ruby': ('#',),
        'php': ('//', '#', '/*'),
        'c': ('//', '/*', '*'),
        'cpp': ('//', '/*', '*'),
        'csharp': ('//',),
    }
    prefixes = comment_prefixes.get(language, ('//', '#'))

    # Detect comment lines
    for line in lines:
        stripped = line.strip()
        if any(stripped.startswith(p) for p in prefixes):
            comment_lines += 1

    # Detect deeply nested code (indentation proxy for complexity)
    for line in lines:
        if line.strip():
            indent = len(line) - len(line.lstrip())
            max_indent = max(max_indent, indent)

    # Detect suspiciously large functions/methods
    fn_patterns = [
        r'^\s*(def |async def |function |const .+ = .*(=>|\() |func |\w+ \w+\()',
    ]
    fn_start_lines = []
    for i, line in enumerate(lines):
        for pat in fn_patterns:
            if re.match(pat, line):
                fn_start_lines.append(i)

    for idx, start in enumerate(fn_start_lines):
        end = fn_start_lines[idx + 1] if idx + 1 < len(fn_start_lines) else total_lines
        fn_length = end - start
        if fn_length > 50:
            long_functions.append({
                "approximate_start_line": start + 1,
                "approximate_length_lines": fn_length,
                "first_line": lines[start].strip()[:100]
            })

    code_lines = total_lines - blank_lines - comment_lines
    comment_ratio = round(comment_lines / total_lines, 3) if total_lines else 0

    return {
        "total_lines": total_lines,
        "code_lines": code_lines,
        "blank_lines": blank_lines,
        "comment_lines": comment_lines,
        "comment_ratio": comment_ratio,
        "max_indentation_depth": max_indent // 4,
        "long_functions_detected": long_functions,
        "long_function_count": len(long_functions)
    }


# Patterns that mark the start of a logical block in various languages
LOGICAL_BOUNDARY_PATTERNS = [
    r'^\s*(def |async def )',
    r'^\s*(class )',
    r'^\s*(export (default |const |function |class ))',
    r'^\s*(function )',
    r'^\s*(const \w+ = \(|const \w+ = async)',
    r'^\s*(public |private |protected |static )',
    r'^\s*(func )',
    r'^\s*(def |end\b)',
    r'^##+ ',
]


def find_logical_boundaries(lines):
    """Return a sorted list of line indices that start a new logical block."""
    boundaries = [0]
    for i, line in enumerate(lines):
        for pat in LOGICAL_BOUNDARY_PATTERNS:
            if re.match(pat, line):
                if i not in boundaries:
                    boundaries.append(i)
                break
    return sorted(boundaries)


def _build_context_note(path, lang, chunk_idx, total_chunks,
                         start_line, end_line, signals, is_test, metrics):
    """
    Generate a plain-English note that gets prepended to the Bedrock prompt
    so the model has immediate context without parsing the JSON itself.
    """
    parts = [
        f"File: {path} ({lang})",
        f"Lines {start_line}–{end_line} (chunk {chunk_idx+1} of {total_chunks}).",
    ]
    if is_test:
        parts.append("This is a TEST file — focus on coverage gaps and mock quality.")
    if signals:
        signal_strs = [f"line {s['line_number']}: {s['line_snippet'][:60]}" for s in signals[:5]]
        parts.append(f"Debt signals in this chunk: {'; '.join(signal_strs)}")
    lf = metrics.get("long_function_count", 0)
    if lf:
        parts.append(f"Whole-file note: {lf} oversized function(s) detected.")
    indent = metrics.get("max_indentation_depth", 0)
    if indent >= 4:
        parts.append(f"Max nesting depth: {indent} levels (complexity risk).")
    return " | ".join(parts)


def chunk_code(files, max_chars=3000):
    """
    Smart chunker that splits at logical boundaries (function/class/section starts)
    rather than arbitrary character positions.

    Each chunk carries rich debt metadata so analysis knows exactly what it's
    looking at without needing to re-read the whole file.

    Output schema per chunk:
    {
        "chunk_id":          str
        "file":              str
        "language":          str
        "chunk_index":       int
        "total_chunks":      int
        "start_line":        int
        "end_line":          int
        "code":              str
        "char_count":        int
        "debt_category_hint":str
        "debt_signals":      list
        "file_metrics":      dict
        "is_entry_point":    bool
        "contains_tests":    bool
        "context_note":      str
    }
    """
    chunks = []

    for file in files:
        content = file["content"]
        path = file["path"]
        lang = file["language"]
        debt_hint = file.get("debt_category_hint", "code_quality")
        all_signals = file.get("debt_signals", [])
        metrics = file.get("metrics", {})
        is_test_file = any(t in path.lower() for t in ['test', 'spec', '__tests__', 'mock'])

        lines = content.splitlines(keepends=True)
        boundaries = find_logical_boundaries([l.rstrip('\n') for l in lines])

        # Build groups of lines between boundaries that fit within max_chars
        groups = []
        current_start = 0
        current_lines = []
        current_chars = 0

        i = 0
        while i < len(boundaries):
            boundary = boundaries[i]
            next_boundary = boundaries[i + 1] if i + 1 < len(boundaries) else len(lines)
            block = lines[boundary:next_boundary]
            block_chars = sum(len(l) for l in block)

            if current_chars + block_chars > max_chars and current_lines:
                groups.append((current_start, current_lines))
                current_start = boundary
                current_lines = block
                current_chars = block_chars
            else:
                if not current_lines:
                    current_start = boundary
                current_lines.extend(block)
                current_chars += block_chars
            i += 1

        if current_lines:
            groups.append((current_start, current_lines))

        total_chunks = len(groups)

        for chunk_idx, (start_line_0, chunk_lines) in enumerate(groups):
            code_text = ''.join(chunk_lines)
            start_line_1 = start_line_0 + 1
            end_line_1 = start_line_0 + len(chunk_lines)

            # Only include debt signals that fall within this chunk's line range
            chunk_signals = [
                s for s in all_signals
                if start_line_1 <= s["line_number"] <= end_line_1
            ]

            context_note = _build_context_note(
                path, lang, chunk_idx, total_chunks,
                start_line_1, end_line_1, chunk_signals, is_test_file, metrics
            )

            chunks.append({
                "chunk_id": f"{path}::chunk_{chunk_idx}",
                "file": path,
                "language": lang,
                "chunk_index": chunk_idx,
                "total_chunks": total_chunks,
                "start_line": start_line_1,
                "end_line": end_line_1,
                "code": code_text,
                "char_count": len(code_text),
                "debt_category_hint": debt_hint,
                "debt_signals": chunk_signals,
                "file_metrics": metrics,
                "is_entry_point": chunk_idx == 0,
                "contains_tests": is_test_file,
                "context_note": context_note
            })

    return chunks


if __name__ == "__main__":
    print("Testing Enhanced Chunking Logic...")
    sample_files = [{
        "path": "test.py",
        "language": "python",
        "content": "def hello():\n    pass\n" * 100,
        "debt_category_hint": "code_quality",
        "debt_signals": [],
        "metrics": {
            "total_lines": 200,
            "code_lines": 200,
            "blank_lines": 0,
            "comment_lines": 0,
            "comment_ratio": 0,
            "max_indentation_depth": 1,
            "long_functions_detected": [],
            "long_function_count": 0
        }
    }]
    
    chunks = chunk_code(sample_files, max_chars=1000)
    print(f"Created {len(chunks)} chunks.")
    if chunks:
        print(f"First chunk: {chunks[0]['chunk_id']}")
        print(f"Chunk count: {len(chunks)}")
