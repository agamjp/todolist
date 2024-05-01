from modules import dict, todolist_functions as tdf
from modules.file_functions import get_todos


def todolist_viewer():
    """Viewer mode, started in case of giving a non-matching password"""
    tasklist = get_todos()
    length = len(tasklist)
    while True:
        print(dict.count_msg.format(t=length))
        if length == 0:
            print(dict.nothing_msg)
            exit()
        else:
            user_action = input(dict.viewer_start_prompt)
            match user_action:
                # można przerobić na if else i podpiąć słownik
                case 'show' | 'display':
                    tdf.todolist_display(tasklist)
                case 'exit':
                    break
                case _:
                    print(dict.invalid_msg)
        return tasklist
