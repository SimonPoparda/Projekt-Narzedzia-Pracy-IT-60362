import argparse
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

if sys.version_info < (3, 9):
    sys.exit("Error: Python 3.9 or higher is required.")

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
    except OSError as e:
        print(f"Error: cannot read '{path}': {e}")
        sys.exit(1)


def load_yaml(path: Path) -> object:
    try:
        with open(path, encoding='utf-8') as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        print(f"Error: invalid YAML in '{path}': {e}")
        sys.exit(1)
    except OSError as e:
        print(f"Error: cannot read '{path}': {e}")
        sys.exit(1)


def _elem_to_dict(elem: ET.Element) -> object:
    children = list(elem)
    if not children and not elem.attrib:
        # ponytail: `or None` normalizes whitespace-only text to None, same as truly empty
        return (elem.text.strip() or None) if elem.text else None

    result = {}
    if elem.attrib:
        result['@attributes'] = dict(elem.attrib)

    for child in children:
        tag = child.tag
        value = _elem_to_dict(child)
        if tag in result:
            if not isinstance(result[tag], list):
                result[tag] = [result[tag]]
            result[tag].append(value)
        else:
            result[tag] = value

    if elem.text and elem.text.strip():
        result['#text'] = elem.text.strip()

    # ponytail: elem.tail (text after closing tag) is not captured — known limitation for mixed-content XML
    return result


def load_xml(path: Path) -> object:
    try:
        tree = ET.parse(path)
    except ET.ParseError as e:
        print(f"Error: invalid XML in '{path}': {e}")
        sys.exit(1)
    except OSError as e:
        print(f"Error: cannot read '{path}': {e}")
        sys.exit(1)
    root = tree.getroot()
    return {root.tag: _elem_to_dict(root)}


def save_json(data: object, path: Path) -> None:
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except OSError as e:
        print(f"Error: cannot write '{path}': {e}")
        sys.exit(1)


def save_yaml(data: object, path: Path) -> None:
    try:
        with open(path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, allow_unicode=True, default_flow_style=False)
    except OSError as e:
        print(f"Error: cannot write '{path}': {e}")
        sys.exit(1)


def _dict_to_elem(tag: str, data: object) -> ET.Element:
    elem = ET.Element(tag)
    if isinstance(data, dict):
        if '@attributes' in data:
            for attr_key, attr_val in data['@attributes'].items():
                elem.set(attr_key, str(attr_val))
        if '#text' in data:
            elem.text = str(data['#text'])
        for key, value in data.items():
            if key in ('@attributes', '#text'):
                continue
            if isinstance(value, list):
                for item in value:
                    elem.append(_dict_to_elem(key, item))
            else:
                elem.append(_dict_to_elem(key, value))
    elif data is not None:
        elem.text = str(data)
    return elem


def save_xml(data: object, path: Path) -> None:
    if not isinstance(data, dict) or len(data) != 1:
        print("Error: XML output requires a dict with exactly one root key.")
        sys.exit(1)
    root_tag, root_data = next(iter(data.items()))
    try:
        root_elem = _dict_to_elem(root_tag, root_data)
        tree = ET.ElementTree(root_elem)
        ET.indent(tree)
        tree.write(path, encoding='utf-8', xml_declaration=True)
    except OSError as e:
        print(f"Error: cannot write '{path}': {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: failed to serialize data to XML: {e}")
        sys.exit(1)


def load_file(path: Path) -> object:
    fmt = get_format(path)
    if fmt == '.json':
        return load_json(path)
    if fmt in ('.yml', '.yaml'):
        return load_yaml(path)
    if fmt == '.xml':
        return load_xml(path)
    print(f"Error: loading '{fmt}' not yet implemented.")
    sys.exit(1)


def save_file(data: object, path: Path) -> None:
    fmt = get_format(path)
    if fmt == '.json':
        save_json(data, path)
        return
    if fmt in ('.yml', '.yaml'):
        save_yaml(data, path)
        return
    if fmt == '.xml':
        save_xml(data, path)
        return
    print(f"Error: saving '{fmt}' not yet implemented.")
    sys.exit(1)


def parse_args():
    parser = argparse.ArgumentParser(
        description='Convert data files between JSON, XML, and YAML formats.',
        usage='converter.exe input.x output.y'
    )
    parser.add_argument('input', type=Path, help='source file (json/xml/yml/yaml)')
    parser.add_argument('output', type=Path, help='destination file (json/xml/yml/yaml)')
    args = parser.parse_args()

    if not args.input.is_file():
        print(f"Error: '{args.input}' does not exist or is not a file.")
        sys.exit(1)

    get_format(args.input)
    get_format(args.output)

    return args.input, args.output


if __name__ == '__main__':
    input_path, output_path = parse_args()
    data = load_file(input_path)
    save_file(data, output_path)
    print(f"Converted '{input_path}' -> '{output_path}'.")
