import argparse
from pathlib import Path
from .core import generate_markdown

def main():
    parser = argparse.ArgumentParser(description='Generate markdown documentation of all files in a directory.')
    parser.add_argument('-s', '--source', required=True, help='Source directory to scan')
    parser.add_argument('-o', '--output', required=True, help='Output markdown file path')
    parser.add_argument('-i', '--ignore', help='Comma-separated list of patterns to ignore')
    
    args = parser.parse_args()
    
    if not Path(args.source).is_dir():
        print(f"Error: Source directory '{args.source}' does not exist.")
        return
    
    print(f"Generating documentation from {args.source} to {args.output}...")
    generate_markdown(args.source, args.output, args.ignore)
    print("Documentation generated successfully.")

if __name__ == '__main__':
    main()