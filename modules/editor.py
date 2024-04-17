from modules import dict, todolist_functions as tdf
from modules.file_functions import get_todos


def todolist_editor():
    """ Editor mode of the todo list (password protected).
    Available actions: show, edit, complete (only if there are items on the list),
    add, exit (always)."""
    tasklist = get_todos()
    while True:
        length = len(tasklist)
        print(dict.count_msg.format(t=length))
        if length == 0:
            user_action = input(dict.start_prompt0)
        else:
            user_action = input(dict.start_prompt1)
        user_action = user_action.strip()
        user_action = user_action.casefold()

        if user_action.startswith(dict.add):
            tdf.todolist_add(tasklist, user_action)
        elif user_action.startswith(dict.show) or user_action.startswith(dict.display):
            tdf.todolist_display(tasklist)
        elif user_action.startswith(dict.edit):
            try:
                tdf.todolist_edit(tasklist, user_action)
            except ValueError:
                print(dict.invalid_msg)
                continue
            except IndexError:
                print(dict.no_number_msg)
                continue
        elif user_action.startswith(dict.complete):
            try:
                tdf.todolist_complete(tasklist, user_action)
            except ValueError:
                print(dict.invalid_msg)
                continue
            except IndexError:
                print(dict.no_number_msg)
                continue
        elif user_action.startswith(dict.exit_):
            break
        else:
            print(dict.invalid_msg)
    return tasklist
