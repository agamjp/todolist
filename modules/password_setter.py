from modules import dict
import PySimpleGUI as sg
import os

label_pswrd = sg.Text(dict.password_prompt)
input_pswrd = sg.InputText(tooltip=dict.password, key="current_password", password_char='*')
wrong_label = sg.Text("", colors="red", key="wrong")

label0_set = sg.Text(dict.set_password_prompt)
input_box_set = sg.InputText(tooltip=dict.password, key="password", password_char='*')
input_box_set1 = sg.InputText(tooltip=dict.password, key="password1", password_char='*')
enter_button_set = sg.Button(dict.set_button)
match_label = sg.Text("", colors="red", key="match")
cancel_button_set = sg.Button(dict.cancel_button)

if os.path.exists("password.txt"):
    layout = [[label_pswrd],
              [input_pswrd],
              [wrong_label],
              [label0_set],
              [input_box_set],
              [input_box_set1, enter_button_set],
              [match_label],
              [cancel_button_set]]
    with open("password.txt", 'r') as file:
        password = file.read()
else:
    layout = [[label0_set],
              [input_box_set],
              [input_box_set1, enter_button_set],
              [match_label],
              [cancel_button_set]]

window_set = sg.Window(dict.editor_head,
                       layout=layout,
                       font=('GeorgiaPro', 20))


def set_password(filepath="password.txt"):
    while True:
        event, values = window_set.read()
        match event:
            case "Set":
                if values["password"] == values["password1"]:
                    with open(filepath, "w") as file:
                        file.write(values["password"])
                    break
                else:
                    window_set["match"].update(dict.match_msg)
            case "Cancel" | sg.WIN_CLOSED:
                break
    window_set.close()

