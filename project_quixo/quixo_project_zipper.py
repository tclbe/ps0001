# written by caleb
# run the file.

import ast, os, sys, zipfile
from pathlib import Path
from typing import BinaryIO, Dict, List

script_dir = Path(__file__).parent

expected_filename = 'quixo.py'

filename = input(
    "enter submission filename (include the '.py', defaults to '{expected_filename}''): "
)

if not filename:
    filename = expected_filename
elif filename != expected_filename:
    print(
        f"\033[91mWARNING:\033[0m the filename should be '{expected_filename}', you input '{filename}'"
    )
    user_in = input("enter 'y' to confirm to continue: ")
    if user_in.upper() != 'Y':
        print("exiting...")
        sys.exit()

filepath = script_dir / filename

if not os.path.exists(filepath):
    print(
        "{filename} not found - make sure the file is in the same folder as this script"
    )
    if os.path.exists(script_dir / (filename + '.py')):
        print(
            f"{filename}.py found - you should remove the .py in the filename."
        )
    print("exiting...")
    sys.exit()

filepath = script_dir / filename


def get_function_byte_positions(
    file: BinaryIO,  # Strictly requires binary mode file object
    encoding: str = 'utf-8'
) -> List[Dict[str, int]]:
    binary_data = file.read()
    source = binary_data.decode(encoding)

    tree = ast.parse(source)

    # Calculate actual byte offsets from raw binary data
    lines = binary_data.splitlines(keepends=True)
    line_offsets = [0]
    for line in lines[:-1]:
        line_offsets.append(line_offsets[-1] + len(line))

    functions = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            # Get text positions from AST
            start_line, start_col = node.lineno, node.col_offset
            end_line, end_col = getattr(node, 'end_lineno',
                                        0), getattr(node, 'end_col_offset', 0)
            if not end_line: continue  # Skip incomplete nodes

            # Convert text positions to byte positions
            start_prefix = source.splitlines()[start_line - 1][:start_col]
            start_byte = line_offsets[start_line - 1] + len(
                start_prefix.encode(encoding))

            end_prefix = source.splitlines()[end_line - 1][:end_col]
            end_byte = line_offsets[end_line - 1] + len(
                end_prefix.encode(encoding))

            functions.append({
                'name': node.name,
                'start_byte': start_byte,
                'end_byte': end_byte
            })

    return functions


def display_function(function: dict, file: BinaryIO):
    if "name" not in func or "start_byte" not in func or "end_byte" not in func:
        raise ValueError("function data not found! missing keys.")
    file.seek(function['start_byte'])
    function_bytes = file.read(function['end_byte'] - function['start_byte'])
    print(function_bytes.decode('utf-8'))


with open(filepath, 'rb') as f:
    functions = get_function_byte_positions(f)

    print("--- checking file contents ---")
    print("enter a number to check a function's contents.")
    print("ENSURE THAT YOU HAVE THE CORRECT FILE BEFORE CONTINUING.")
    user_in = -1
    while user_in != 'c':
        print(f"{len(functions)} functions found:")
        for i, func in enumerate(functions):
            print(f"{i+1}: {func['name']}")
        user_in = input(
            "enter a number to check a function, or enter 'c' to continue: ")

        if user_in == 'c':
            break

        try:
            user_in = int(user_in)
            display_function(functions[user_in - 1], f)
        except:
            print("enter a number or 'c'!")

    print("--- time to make a zip file ---")
    user_in = -1
    matric_nos = []
    while user_in != 'c':
        print(f"current matric nos: {', '.join(matric_nos)}")

        user_in = input(
            "enter a matric number (enter 'c' to finish, 'r' to remove): ")

        if user_in == 'c':
            break
        elif user_in == 'r':
            to_remove = -1
            for i, matric_no in enumerate(matric_nos):
                print(f"{i+1}: {matric_no}")
            to_remove = input("enter number to remove, or 'c' to go back: ")

            if to_remove == "c": continue

            try:
                to_remove = int(to_remove)
                print(f"{matric_nos.pop(to_remove-1)} removed")
            except:
                print("enter a number or 'c'!")
            continue

        if len(user_in) != 9:
            print("the matric number entered did not have 9 characters!")
        else:
            matric_nos.append(user_in.upper())

    zipfilepath = script_dir / ("_".join(matric_nos) + '.zip')

    if os.path.exists(zipfilepath):
        user_in = input(
            f"filename {zipfilepath} already exists! enter 'y' to confirm overwrite: "
        )
        if user_in.upper() != 'Y':
            print("exiting...")
            sys.exit()

    with zipfile.ZipFile(zipfilepath, 'w') as zipf:
        zipf.write(filepath, arcname=filepath.name)

    print(f"{zipfilepath} written successfully, ready for submission.")
