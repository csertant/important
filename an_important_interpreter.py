"""---------------------------------------------------------------------------------------\
|    This is An IMPORTANT Interpreter & Compiler for the IMPORTANT language               |
-----------------------------------------------------------------------------------------|
Version: 1.0.alpha
"""

import sys
import argparse
from collections import deque
from important_cleaning import important_clean_program, important_get_fileinfo


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
    parser.add_argument(
        '-m', '--mode', choices=['compile', 'interpret'],
        type=str, required=True, help='compiler or interpreter mode'
    )
    parser.add_argument(
        '-o', '--output', type=str,
        help='output file name (extension will be .c)'
    )
    parser.add_argument(
        'filename', type=str, nargs=1,
        help='file to execute'
    )
    return parser


def parse_file(filename) -> str:
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read().replace("\n", "")
    return content


def run_code(code_string) -> int:
    """Executes program."""
    exit_code = 0

    cleaned_code_string = important_clean_program(code_string)

    return exit_code


def compile_code(code_string) -> (str, int):
    """Compiles program to C language."""
    exit_code = 0
    compiled = ''

    return compiled, exit_code


def save_compiled_code(compiled_code_str, file) -> None:
    """Saves compiled code to file"""
    path, name = important_get_fileinfo(file)
    print(f"Saving to {file}...")


def main() -> None:
    parser = init_parser()
    args = parser.parse_args()

    filename = args.filename[0]
    try:
        content = parse_file(filename)
    except (FileNotFoundError, IsADirectoryError, PermissionError) as err:
        raise SystemExit(f"[{sys.argv[0]}] {filename}: {err.strerror}")

    mode = args.mode
    if 'interpret' in mode:
        exit_code = run_code(content)
        raise SystemExit(f"[interpreter] Process finished with exit code {exit_code}.")
    elif 'compile' in mode:
        output = args.output if args.output is not None else filename
        compiled_code, exit_code = compile_code(content)
        save_compiled_code(compiled_code, output)
        raise SystemExit(f"[compiler] Process finished with exit code {exit_code}.")


if __name__ == '__main__':
    main()
