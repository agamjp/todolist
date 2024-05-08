from modules import dict, editor, viewer
import os
from dotenv import load_dotenv

load_dotenv()


def initiate():
    """ Prompt for password and open the todo list
    in editor mode if the password matches
    or in viewer mode if it doesn't """
    print(dict.greeting_msg)
    while True:
        if os.getenv("PASSWORD") is not None:
            password = os.getenv("PASSWORD")
            user_pass = input(dict.password_prompt)
            if user_pass == password:
                editor.todolist_editor()
                break
            else:
                print(dict.wrong_password_msg)
                viewer.todolist_viewer()
                break
        else:
            editor.todolist_editor()
    print(dict.goodbye_msg)


initiate()

