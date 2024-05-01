import os
import sys

FILEPATH = 'todos.txt'


def get_todos(path=FILEPATH):
    with open(path, "r") as file:
        tasklist = file.readlines()
    return tasklist


def write_todos(todolist, path=FILEPATH):
    with open(path, "w") as file:
        file.writelines(todolist)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    print(get_todos())
