from pathlib import Path

DEFAULT_EXTENSION = '.c'
CHARACTER_SET = ['<', '>', '+', '-', '.', ',', 'ˇ', '^', ';', '{', '}']


def important_clean_program(program_string: str) -> str:
    cleaned_string = ""
    is_comment = False
    for char in program_string:
        if char == ':' and not is_comment:
            is_comment = True
            continue
        if char == ':' and is_comment:
            is_comment = False
            continue
        if is_comment and char in CHARACTER_SET:
            cleaned_string += char
    return cleaned_string


def important_get_file_info(filepath: str, input_name: str) -> (str, str):
    """Gets path and name from file string"""
    p = Path(filepath)
    input_name = Path(input_name).stem

    if p.is_dir():
        path = filepath
        name = input_name + DEFAULT_EXTENSION
        return path, name
    elif p.is_file():
        path = str(p.parent)
        name = p.name
        if p.suffix == '':
            name += DEFAULT_EXTENSION
        return path, name
    elif p.parent.is_dir():
        path = str(p.parent)
        name = p.stem + DEFAULT_EXTENSION
        return path, name
    else:
        raise FileNotFoundError('No such file or directory.')
