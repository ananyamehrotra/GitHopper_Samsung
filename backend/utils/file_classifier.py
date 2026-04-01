def classify_file(filepath):
    """
    Classify a file based on its path and extension.
    Returns one of: 'app', 'iac', 'iam', 'deps', or 'unknown'
    """
    filepath_lower = filepath.lower()
    
    # Application code (Python files)
    if filepath.endswith('.py'):
        return 'app'
    
    # Infrastructure as Code
    if filepath.endswith('.tf') or filepath.endswith('.yaml') or filepath.endswith('.yml'):
        return 'iac'
    
    # IAM policies (JSON files in iam directory)
    if 'iam' in filepath_lower and filepath.endswith('.json'):
        return 'iam'
    
    # Dependencies (requirements.txt, package.json, etc.)
    if filepath.endswith('.txt') or (filepath.endswith('.json') and 'package' in filepath_lower):
        return 'deps'
    
    # Default
    return 'unknown'