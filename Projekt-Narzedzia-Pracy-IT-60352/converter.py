import argparse
import json
import sys
from pathlib import Path

SUPPORTED_FORMATS = {'.json', '.xml', '.yml', '.yaml'}


def get_format(path: Path) -> str:
    ext = path.suffix.lower()
    if ext not in SUPPORTED_FORMATS:
        print(f"Error: unsupported format '{ext}'. Supported: {', '.join(sorted(SUPPORTED_FORMATS))}")
        sys.exit(1)
    return ext


def load_json(path: Path) -> object:
    try:
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: invalid JSON in '{path}': {e}")
        sys.exit(1)


def load_file(path: Path) -> object:
    fmt = get_format(path)
    if fmt == '.json':
        return load_json(path)
    print(f"Error: loading '{fmt}' not yet implemented.")
    sys.exit(1)


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
    data = load_file(input_path)
    print(f"Loaded {type(data).__name__} from '{input_path}'.")
    print("Conversion not yet implemented.")
