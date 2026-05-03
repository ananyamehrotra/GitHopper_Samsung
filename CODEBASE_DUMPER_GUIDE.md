# 📚 Codebase Dumper Guide

This tool automatically consolidates your entire codebase into a single, easy-to-read markdown file.

## What It Does

The codebase dumper scans your entire project and creates `CODEBASE_DUMP.md` containing:
- ✨ A complete table of contents
- 📂 All source code files with proper syntax highlighting
- 📊 File sizes and organization
- 🔍 Easy searchable reference of your entire codebase

## Setup

### First Time Setup

The dumper scripts are already included in the repository:

- **Windows:** `update_codebase_dump.bat`
- **macOS/Linux:** `update_codebase_dump.sh`
- **Python Script:** `codebase_dumper.py`

No additional installation needed!

## How to Use

### Windows Users

Simply double-click the batch file:
```
update_codebase_dump.bat
```

Or run from command prompt:
```cmd
update_codebase_dump.bat
```

### macOS/Linux Users

Run the shell script from terminal:
```bash
bash update_codebase_dump.sh
```

Or make it executable first:
```bash
chmod +x update_codebase_dump.sh
./update_codebase_dump.sh
```

### Manual Python Execution (All Platforms)

```bash
python3 codebase_dumper.py
```

## Output

After running, you'll get:
- ✅ `CODEBASE_DUMP.md` - Complete codebase in one file
- 📊 File count and total size information
- ⏱️ Generation timestamp

## What Gets Included

**Included file types:**
- Python files (`.py`)
- JavaScript/TypeScript (`.js`, `.jsx`, `.ts`, `.tsx`)
- Web files (`.html`, `.css`, `.scss`)
- Configuration (`.json`, `.yaml`, `.yml`, `.toml`)
- Documentation (`.md`, `.txt`)
- Scripts (`.sh`, `.bat`, `.dockerfile`)

**Excluded directories:**
- `node_modules/` - npm dependencies
- `venv/` / `env/` - Python virtual environments
- `.git/` - Git history
- `__pycache__/` - Python cache
- `dist/` / `build/` - Build outputs
- `mcp_data/` - Data files
- `scan_results/` - Result files
- `.env` - Secret environment files
- `public/` - Static assets

## Automation

### Auto-Update on Commit (Git Hook)

Create a `.git/hooks/post-commit` file (no extension):

**For macOS/Linux:**
```bash
#!/bin/bash
python3 codebase_dumper.py
git add CODEBASE_DUMP.md
```

**For Windows PowerShell:**
```powershell
python3 codebase_dumper.py
git add CODEBASE_DUMP.md
```

Then make it executable:
```bash
chmod +x .git/hooks/post-commit
```

### Scheduled Updates

**Windows Task Scheduler:**
1. Open Task Scheduler
2. Create Basic Task
3. Trigger: Daily at your preferred time
4. Action: `update_codebase_dump.bat`

**macOS/Linux Cron:**
```bash
# Daily at 2 AM
0 2 * * * cd /path/to/githoppermain && bash update_codebase_dump.sh
```

## Using CODEBASE_DUMP.md

### View in VS Code
- Open `CODEBASE_DUMP.md` in the editor
- Use Ctrl+F (Cmd+F on Mac) to search
- Use breadcrumbs to navigate sections

### View in Browser
- Open the file with your markdown renderer
- Many online viewers support markdown files
- GitHub automatically renders it

### Share with Team
- Commit to repository for team access
- Use as documentation reference
- Share with AI assistants for context

## Troubleshooting

### "Python not found"
Install Python 3.8+ from [python.org](https://www.python.org)

### File is too large
The dump can be large for big projects. You can:
- Open in VS Code (optimized for large files)
- Use a markdown viewer that handles large files
- Search within VS Code using Ctrl+F

### Permissions Error (macOS/Linux)
```bash
chmod +x update_codebase_dump.sh
./update_codebase_dump.sh
```

## Performance Notes

- **Small projects (<1000 files):** < 1 second
- **Medium projects:** 1-5 seconds
- **Large projects:** 5-30 seconds

The dump is read-only and won't modify your source code.

## Examples

### Search for a Function
Open `CODEBASE_DUMP.md` and use Ctrl+F to find your function:
```
Ctrl+F → "def my_function"
```

### Browse Organization
Check the table of contents to see project structure at a glance.

### Share with AI
Copy relevant sections of the dump to:
- GitHub Copilot
- Claude
- ChatGPT
- Other AI assistants

## Pro Tips

1. **Commit regularly** - The dump shows code at generation time
2. **Use with version control** - Compare dumps to see what changed
3. **Share with new team members** - Great onboarding reference
4. **Include in documentation** - Link to specific sections
5. **Archive old dumps** - Keep history of project evolution

## Advanced Configuration

To customize what gets included, edit `codebase_dumper.py`:

```python
# Line ~20: Add extensions to INCLUDE_EXTENSIONS
INCLUDE_EXTENSIONS = {
    '.py', '.js', '.ts',  # Add your custom extensions here
}

# Line ~30: Add folders to EXCLUDE_DIRS
EXCLUDE_DIRS = {
    'folder_to_skip',
    'another_folder',
}
```

---

**Happy coding!** 🚀

For updates to the dumper, check the main repository.
