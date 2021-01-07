"""---------------------------------------------------------------------------------------\
|    This is An IMPORTANT Interpreter & Compiler for the IMPORTANT language               |
-----------------------------------------------------------------------------------------|
Version: 1.0.alpha
"""

import sys
import os
import argparse
from collections import deque
from important_cleaning import important_clean_program, important_get_file_info
from important_operations import execute, MEMORY_SIZE, MAX_STACK_SIZE, important_compile


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


def parse_file(filename: str) -> str:
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read().replace("\n", "")
    return content


def run_code(code_string: str) -> int:
    """Executes program."""
    exit_code = 0

    cleaned_code = important_clean_program(code_string)

    # Process operations
    try:
        execute(cleaned_code)
    except SyntaxError as err:
        print("[interpreter] Error: {}".format(err))
        return 1
    except ValueError as err:
        print(err.with_traceback(err.__traceback__))
        return 2
    except EOFError:
        print("[interpreter] Unexpected end of file.")
        return 100
    except KeyboardInterrupt:
        raise SystemExit("[interpreter] You exited. Bye!")

    return exit_code


def compile_code(code_string: str) -> (str, int):
    """Compiles program to C language."""
    exit_code = 0

    cleaned_code = important_clean_program(code_string)

    try:
        compiled = important_compile(cleaned_code)
    except SyntaxError as err:
        print("[compiler] Error: {}".format(err))
        compiled = None
        exit_code = 1

    return compiled, exit_code


def save_compiled_code(compiled_code_str: str, input_file: str, output_file: str) -> None:
    """Saves compiled code to file"""
    path, name = important_get_file_info(output_file, input_file)
    print(f"[compiler] Saving to {path}\\{name}...")
    with open(os.path.join(path, name), "w") as outfile:
        outfile.write(compiled_code_str)


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
        if exit_code != 0:
            raise SystemExit(f"[compiler] Process finished with exit code {exit_code}.")
        save_compiled_code(compiled_code, filename, output)
        raise SystemExit(f"[compiler] Process finished with exit code {exit_code}.")


if __name__ == '__main__':
    main()
