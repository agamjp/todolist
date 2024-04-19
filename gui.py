from modules import dict, todolist_functions as tdf
from modules.file_functions import get_todos, write_todos
import PySimpleGUI as sg

label0 = sg.Text(dict.password_prompt)
input_box0 = sg.InputText(tooltip=dict.enter, key="password", password_char='*')
enter_button = sg.Button(dict.enter_button)

input_box = sg.InputText(tooltip=dict.enter, key="todo")
add_button = sg.Button(dict.add_button)

edit_button = sg.Button(dict.edit_button)

exit_button0 = sg.Button(dict.exit_button)
exit_button = sg.Button(dict.exit_button)

window0 = sg.Window(dict.editor_head,
                    layout=[[label0], [input_box0, enter_button],
                            [exit_button0]],
                    font=('GeorgiaPro', 20))
event, values = window0.read()
layout = []
with open("password.txt", "r") as keyfile:
    password = keyfile.read()
user_pass = values['password']
match event:
    case "Enter":
        if user_pass == password:
            list_box = sg.Listbox(values=get_todos(), key='todos',
                                  enable_events=True, size=(45, 10))
            label = sg.Text(dict.todo_prompt)
            layout = [[label], [input_box, add_button],
                      [list_box, edit_button],
                      [exit_button]]
        else:
            list_box = sg.Listbox(values=get_todos(), key='todos',
                                  enable_events=False, size=(45, 10))
            # may chance to True if I add possibility to complete for viewers
            label = sg.Text(dict.viewer_mode_msg)
            layout = [[label],
                      [list_box],
                      [exit_button]]
    case "Exit" | sg.WIN_CLOSED:
        exit("Bye")
window0.close()

window = sg.Window(dict.editor_head,
                   layout=layout,
                   font=('GeorgiaPro', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    print(list_box.get_indexes())
    match event:
        case "Add":
            todolist = get_todos()
            new_todo = "add " + values['todo']
            tdf.todolist_add(todolist, new_todo)
            window['todos'].update(values=todolist)
        case "Edit":
            todo = values['todos']
            new_todo = values['todo'].capitalize() + '\n'
            todolist = get_todos()
            index = list_box.get_indexes()[0]
            todolist[index] = new_todo
            write_todos(todolist)
            window['todos'].update(values=todolist)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case "Exit" | sg.WIN_CLOSED:
            break

window.close()
