import os
from pathlib import Path


def should_ignore(file_path, ignore_patterns):
    """Check if a file should be ignored based on ignore patterns"""
    for pattern in ignore_patterns:
        if pattern in str(file_path):
            return True
    return False


def process_file(file_path):
    """Read and format a file's content for markdown output"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        return f"```{Path(file_path).suffix[1:] if Path(file_path).suffix else ''}\n{content}\n```"
    except UnicodeDecodeError:
        return f"*[Binary file - content not displayed]*"
    except Exception as e:
        return f"*[Error reading file: {str(e)}]*"


def generate_markdown(source_dir, output_file, ignore_patterns):
    """Generate markdown documentation of all files"""
    ignore_list = (
        [p.strip() for p in ignore_patterns.split(",")] if ignore_patterns else []
    )

    with open(output_file, "w", encoding="utf-8") as md_file:
        for root, dirs, files in os.walk(source_dir):
            # Remove ignored directories from traversal
            dirs[:] = [
                d for d in dirs if not should_ignore(os.path.join(root, d), ignore_list)
            ]

            for file in files:
                file_path = os.path.join(root, file)
                if should_ignore(file_path, ignore_list):
                    continue

                relative_path = os.path.relpath(file_path, source_dir)
                md_file.write(f"// {relative_path}\n")
                md_file.write(process_file(file_path))
                md_file.write("\n\n")
