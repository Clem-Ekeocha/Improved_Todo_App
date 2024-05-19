def get_todos(filepath="todos.txt"):  # Create a custom function that opens the todos the textfile
    """
    Read a text file and return the list of to-do items.
    """
    with open(filepath, 'r') as file:
        todos = file.readlines()
    return todos


def write_todos(filepath, todos_arg):  # Create a custom function that writes on a textfile
    """
    Write a new to-do to the list of to-dos in the textfile.
    """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())