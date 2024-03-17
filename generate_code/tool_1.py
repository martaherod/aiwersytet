import ast
from ast import parse, walk, get_docstring


def get_functions_from_file(filename):
    with open('code/ex_2.py', 'r') as file:
        tree = parse(file.read())
        for node in walk(tree):
            if isinstance(node, ast.FunctionDef):
                yield node

for function in get_functions_from_file('code/ex_2.py'):
    print(f'Function name: {function.name}')
    print(f'Function doctstring: {get_docstring(function)}')