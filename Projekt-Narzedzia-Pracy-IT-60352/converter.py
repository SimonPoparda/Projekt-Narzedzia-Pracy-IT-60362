import argparse
import sys
from pathlib import Path

SUPPORTED_FORMATS = {'.json', '.xml', '.yml', '.yaml'}


def get_format(path: Path) -> str:
    ext = path.suffix.lower()
    if ext not in SUPPORTED_FORMATS:
        print(f"Error: unsupported format '{ext}'. Supported: {', '.join(sorted(SUPPORTED_FORMATS))}")
        sys.exit(1)
    return ext


def parse_args():
    parser = argparse.ArgumentParser(
        description='Convert data files between JSON, XML, and YAML formats.',
        usage='converter.exe input.x output.y'
    )
    parser.add_argument('input', type=Path, help='source file (json/xml/yml/yaml)')
    parser.add_argument('output', type=Path, help='destination file (json/xml/yml/yaml)')
    args = parser.parse_args()

    if not args.input.exists():
        print(f"Error: input file '{args.input}' does not exist.")
        sys.exit(1)

    get_format(args.input)
    get_format(args.output)

    return args.input, args.output


if __name__ == '__main__':
    input_path, output_path = parse_args()
    print(f"Input:  {input_path} ({get_format(input_path)})")
    print(f"Output: {output_path} ({get_format(output_path)})")
    print("Conversion not yet implemented.")
