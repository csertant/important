"""----------------------------------------------------------------------------\
|    This is AN IMPORTANT Interpreter for the IMPORTANT language               |
-------------------------------------------------------------------------------|
"""

import sys
import argparse
from collections import deque


def init_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="important_interpreter",
        usage="%(prog)s [file] [options]",
        description="Interpret & execute IMPORTANT code files.",
        fromfile_prefix_chars='@'
    )
    parser.add_argument(
        "-v", "--version", action="version",
        version=f"{parser.prog} version: 1.0.alpha"
    )
    parser.add_argument('filename', type=str, nargs=1, help='file to execute')
    return parser


def parse_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read().replace("\n", "")
    return content


def run_code(code_string):
    pass


def main() -> None:
    parser = init_parser()
    args = parser.parse_args()

    filename = args.filename[0]
    try:
        content = parse_file(filename)
    except (FileNotFoundError, IsADirectoryError, PermissionError) as err:
        raise SystemExit(f"[{sys.argv[0]}] {filename}: {err.strerror}")

    run_code(content)


if __name__ == '__main__':
    main()
