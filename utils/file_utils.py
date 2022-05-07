import pathlib
from os.path import sep as path_separator
from os.path import join as path_join
from os import mkdir


def create_dir_tree(path: str) -> None:
    dir_list = path.split(path_separator)[:-1]
    if len(dir_list) > 0:
        current_path = dir_list[0]
        for current_dir in dir_list:
            if not pathlib.Path(current_path).exists():
                mkdir(current_path)
            current_path = path_join(current_path, current_dir)


def create_file(path: str, data: bytes):
    create_dir_tree(path)
    with pathlib.Path(path).open('wb') as file:
        file.write(data)
