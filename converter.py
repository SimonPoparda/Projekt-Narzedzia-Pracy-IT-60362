import argparse
import json
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

if sys.version_info < (3, 9):
    sys.exit("Error: Python 3.9 or higher is required.")

SUPPORTED_FORMATS = {'.json', '.xml', '.yml', '.yaml'}


class ConverterError(Exception):
    pass


def get_format(path: Path) -> str:
    ext = path.suffix.lower()
    if ext not in SUPPORTED_FORMATS:
        raise ConverterError(
            f"Unsupported format '{ext}'. Supported: {', '.join(sorted(SUPPORTED_FORMATS))}"
        )
    return ext


def load_json(path: Path) -> object:
    try:
        with open(path, encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise ConverterError(f"Invalid JSON in '{path}': {e}")
    except OSError as e:
        raise ConverterError(f"Cannot read '{path}': {e}")


def load_yaml(path: Path) -> object:
    try:
        with open(path, encoding='utf-8') as f:
            return yaml.safe_load(f)
    except yaml.YAMLError as e:
        raise ConverterError(f"Invalid YAML in '{path}': {e}")
    except OSError as e:
        raise ConverterError(f"Cannot read '{path}': {e}")


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

    return result


def load_xml(path: Path) -> object:
    try:
        tree = ET.parse(path)
    except ET.ParseError as e:
        raise ConverterError(f"Invalid XML in '{path}': {e}")
    except OSError as e:
        raise ConverterError(f"Cannot read '{path}': {e}")
    root = tree.getroot()
    return {root.tag: _elem_to_dict(root)}


def save_json(data: object, path: Path) -> None:
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    except OSError as e:
        raise ConverterError(f"Cannot write '{path}': {e}")


def save_yaml(data: object, path: Path) -> None:
    try:
        with open(path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, allow_unicode=True, default_flow_style=False)
    except OSError as e:
        raise ConverterError(f"Cannot write '{path}': {e}")


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
        raise ConverterError("XML output requires a dict with exactly one root key.")
    root_tag, root_data = next(iter(data.items()))
    try:
        root_elem = _dict_to_elem(root_tag, root_data)
        tree = ET.ElementTree(root_elem)
        ET.indent(tree)
        tree.write(path, encoding='utf-8', xml_declaration=True)
    except OSError as e:
        raise ConverterError(f"Cannot write '{path}': {e}")
    except Exception as e:
        raise ConverterError(f"Failed to serialize data to XML: {e}")


def load_file(path: Path) -> object:
    fmt = get_format(path)
    if fmt == '.json':
        return load_json(path)
    if fmt in ('.yml', '.yaml'):
        return load_yaml(path)
    return load_xml(path)


def save_file(data: object, path: Path) -> None:
    fmt = get_format(path)
    if fmt == '.json':
        save_json(data, path)
    elif fmt in ('.yml', '.yaml'):
        save_yaml(data, path)
    else:
        save_xml(data, path)


def convert(input_path: Path, output_path: Path) -> None:
    if not input_path.is_file():
        raise ConverterError(f"'{input_path}' does not exist or is not a file.")
    get_format(input_path)
    get_format(output_path)
    data = load_file(input_path)
    save_file(data, output_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Convert data files between JSON, XML, and YAML formats.',
        usage='converter.exe input.x output.y'
    )
    parser.add_argument('input', type=Path, help='source file (json/xml/yml/yaml)')
    parser.add_argument('output', type=Path, help='destination file (json/xml/yml/yaml)')
    args = parser.parse_args()
    try:
        convert(args.input, args.output)
        print(f"Converted '{args.input}' -> '{args.output}'.")
    except ConverterError as e:
        print(f"Error: {e}")
        sys.exit(1)
