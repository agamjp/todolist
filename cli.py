from modules import dict, editor, viewer
from getpass import getpass
import os


def initiate():
    """ Prompt for password and open the todo list
    in editor mode if the password matches
    or in viewer mode if it doesn't """
    print(dict.greeting_msg)
    while True:
        if os.path.exists("password.txt"):
            with open("password.txt", "r") as keyfile:
                password = keyfile.read()
            user_pass = input(dict.password_prompt)
            if user_pass == password:
                editor.todolist_editor()
                break
            else:
                print(dict.wrong_password_msg)
                viewer.todolist_viewer()
                break
        else:
            while True:
                password = input(dict.set_password_prompt)
                password1 = input("Repeat the new password: ")
                if password1 == password:
                    with open("password.txt", "w") as keyfile:
                        keyfile.write(password)
                        break
                else:
                    print(dict.match_msg)
    print(dict.goodbye_msg)


initiate()

