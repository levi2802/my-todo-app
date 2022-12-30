FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """Reads the textfile"""
    with open(filepath, 'r') as file_local:
        todos = file_local.readlines()
    return todos


# Non default parameters should be placed before the default parameters
def write_todos(todos, filepath=FILEPATH):
    """Write a text to the textfile"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos)
