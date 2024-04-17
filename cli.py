from modules import dict, editor, viewer


def initiate():
    """ Prompt for password and open the todo list
    in editor mode if the password matches
    or in viewer mode if it doesn't """
    print(dict.greeting_msg)
    with open("password.txt", "r") as keyfile:
        password = keyfile.read()
    user_pass = input(dict.password_prompt)
    if user_pass == password:
        editor.todolist_editor()
    else:
        print(dict.wrong_password_msg)
        viewer.todolist_viewer()
    print(dict.goodbye_msg)


initiate()

