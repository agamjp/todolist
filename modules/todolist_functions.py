from modules import dict, file_functions as ff


def todolist_display(todolist):
    """ Show the current todo list """
    print(dict.display_msg)
    # new_list = [item.strip('\n') for item in todolist]
    # ^ list comprehension - unnecessary extra loop but also an option
    for index, item in enumerate(todolist):
        item = item.strip('\n')
        print(f"{index + 1}. {item}")


def todolist_edit(todolist, command):
    """ Edit the entry with the indicated number.
    The number can either directly follow the command
    or be entered later.  In the latter case,
    0 can be typed to display the list before making the choice. """
    if len(command) > 5:
        number = int(command[5:])
    else:
        number = int(input(dict.number_prompt0.format(t=command)))
        if number == 0:
            todolist_display(todolist)
            number = int(input(dict.number_prompt1.format(t=command)))
    index = number - 1
    todo_to_edit = todolist[index]
    print(dict.selected_todo_msg, todo_to_edit)
    edited_todo = input(dict.todo_prompt) + "\n"
    todolist[index] = edited_todo.capitalize()
    ff.write_todos(todolist)
    return todolist


def todolist_complete(todolist, command):
    """ Remove the entry with the indicated number from the list.
    The number can either directly follow the command
    or be entered later. In the latter case,
    0 can be typed to display the list before making the choice. """
    if len(command) > 9:
        number = int(command[9:])
    else:
        number = int(input(dict.number_prompt0.format(t=command)))
        if number == 0:
            todolist_display(todolist)
            number = int(input(dict.number_prompt1.format(t=command)))
    index = number - 1
    completed = todolist[index].strip('\n')
    todolist.pop(index)
    ff.write_todos(todolist)
    print(dict.removed_msg.format(t=completed))
    return todolist


def todolist_add(todolist, command):
    """ Add a new entry to the list.
        The todo content can either directly follow the command
        or be entered later. """
    if len(command) > 4:
        todo = command[4:] + "\n"
    else:
        todo = input(dict.todo_prompt) + "\n"
    todolist.append(todo.capitalize())
    ff.write_todos(todolist)
    return todolist
