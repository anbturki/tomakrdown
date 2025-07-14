# tomarkdown 📂→📝

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A lightweight command-line tool that converts directory structures into well-formatted markdown documentation, preserving file contents with syntax highlighting.

## Features ✨

- **Recursive Directory Scanning**: Processes nested folder structures effortlessly.
- **Syntax Highlighting**: Automatically detects programming languages from file extensions for proper code block formatting.
- **Custom Ignore Patterns**: Exclude specific files or directories using comma-separated patterns.
- **Preserved File Structure**: Outputs relative file paths to maintain project hierarchy.
- **Zero Dependencies**: Built with Python standard library for maximum portability.
- **Cross-Platform**: Compatible with Windows, macOS, and Linux.

## Installation ⚙️

### Prerequisites
- Python 3.8 or higher

### Recommended: pipx (Isolated Installation)
```bash
pipx install tomarkdown
```

### Standard pip Installation
```bash
pip install tomarkdown
```

### From Source (Development)
```bash
git clone https://github.com/anbturki/tomarkdown.git
cd tomarkdown
pip install -e .
```

## Usage 🚀

### Basic Command
```bash
tomarkdown -s ./project -o DOCUMENTATION.md
```

### Advanced Usage with Ignore Patterns
```bash
tomarkdown -s ./src -o ./docs/CODEBASE.md -i "node_modules,.git,__pycache__,*.pyc,*.log"
```

### CLI Options
| Option       | Shorthand | Description                          | Default |
|--------------|-----------|--------------------------------------|---------|
| `--source`   | `-s`      | Source directory to scan             | Required |
| `--output`   | `-o`      | Output markdown file path            | Required |
| `--ignore`   | `-i`      | Comma-separated ignore patterns      | None    |
| `--version`  | `-v`      | Show version and exit                | N/A     |
| `--help`     | `-h`      | Show help message and exit          | N/A     |

## Example Output 📄
The generated markdown will look like this:

```markdown
// src/main.py
```python
def main():
    print("Hello World!")

if __name__ == "__main__":
    main()
```

// utils/helpers.js
```javascript
// Format date as YYYY-MM-DD
function formatDate(d) {
  return d.toISOString().split('T')[0];
}
```

// README.md
```markdown
# Project Title

This is a sample README file...
```
```

## Development 🛠️

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/anbturki/tomarkdown.git
   cd tomarkdown
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install with development dependencies:
   ```bash
   pip install -e .[dev]
   ```

### Running Tests
```bash
pytest tests/
```

### Building for Distribution
```bash
python -m build
```

## FAQ ❓

**Q: How do I exclude multiple patterns?**  
A: Use comma-separated patterns: `-i "node_modules,.git,*.log"`.

**Q: Can I use absolute paths?**  
A: Yes, both relative and absolute paths are supported for source and output.

**Q: What file encodings are supported?**  
A: Files are read as UTF-8. Binary files are skipped with a notice in the output.

## Contributing 🤝

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/your-feature`).
3. Commit your changes (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a Pull Request.

Please ensure your code follows the [Black](https://github.com/psf/black) code style and includes tests where applicable.

## License 📜

MIT License - See [LICENSE](LICENSE) for details.

Created with ❤️ by [Ali Turki](https://github.com/anbturki) - Report issues on [GitHub](https://github.com/anbturki/tomarkdown/issues).
