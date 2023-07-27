import os
import struct

import output


def find_greatest_common_factor(paths):
    # Find the common prefix among all paths
    common_prefix = os.path.commonpath(paths) + "/"

    # Remove the common prefix from each path
    cleaned_paths = [path.replace(common_prefix, "", 1) for path in paths]

    return cleaned_paths, common_prefix


def create_directories(path_list):
    # Remove the last element from the path_list
    path_list = path_list[:-1]

    # Join the elements of the path_list to form the directory path
    dir_path = os.path.join(*path_list)

    # Create the directory and any missing parent directories
    os.makedirs(dir_path, exist_ok=True)


def pad_filename(file_name):
    # Ensure the file name is a string
    file_name = str(file_name)

    # Calculate the number of NULL characters needed for padding
    padding_size = 4096 - len(file_name)

    if padding_size < 0:
        raise ValueError("FILE NAME CANNOT BE THAT LONG")

    # Append NULL characters to the file name to pad it to 4096 bytes
    padded_file_name = file_name + ('\0' * padding_size)

    # Return the padded file name as bytes
    return padded_file_name.encode('utf-8')


def remove_excess_null_chars(bytes_object):
    # Find the index of the first non-NULL character from the end
    last_non_null_index = len(bytes_object) - 1
    while last_non_null_index >= 0 and bytes_object[last_non_null_index] == 0:
        last_non_null_index -= 1

    # Slice the bytes object to remove the excess NULL characters
    cleaned_bytes = bytes_object[:last_non_null_index + 1]

    return cleaned_bytes


def size_to_bytes(file_size: int):
    try:
        return struct.pack(">q", file_size)
    except OverflowError:
        raise ValueError("File too big to add")


def size_from_bytes(file_size: bytes):
    return struct.unpack(">q", file_size)[0]


def print_tree(paths):
    def build_tree(paths):
        tree = {}
        for path in paths:
            parts = path.split('/')
            current = tree
            for part in parts:
                current = current.setdefault(part, {})
        return tree

    def print_directory(tree, indent_level=0):
        for item, subtree in tree.items():
            is_last_item = len(subtree) == 0
            prefix = "|   " * indent_level + "|-- " if indent_level > 0 else ""

            print(prefix + item)
            if not is_last_item:
                print_directory(subtree, indent_level + 1)

    tree = build_tree(paths)
    print_directory(tree)


def try_file_op(operation, message, exit_code=2):
    try:
        operation()
    except (FileNotFoundError, IsADirectoryError, PermissionError):
        output.print_fatal(message)
        exit(exit_code)
