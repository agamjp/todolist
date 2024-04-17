FILEPATH = 'todos.txt'


def get_todos(path=FILEPATH):
    with open(path, "r") as file:
        tasklist = file.readlines()
    return tasklist


def write_todos(todolist, path=FILEPATH):
    with open(path, "w") as file:
        file.writelines(todolist)


if __name__ == "__main__":
    print(get_todos())
