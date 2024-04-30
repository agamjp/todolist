from modules import dict, todolist_functions as tdf
from modules.file_functions import get_todos, write_todos
import PySimpleGUI as sg
import time

sg.theme("BluePurple")

label0 = sg.Text(dict.password_prompt)
input_box0 = sg.InputText(tooltip=dict.password, key="password", password_char='*')
enter_button = sg.Button(dict.enter_button)

clock = sg.Text('', key='clock')
add_button = sg.Button(dict.add_button)

list_box = sg.Listbox(values=get_todos(), key='todos', enable_events=True, size=(45, 10))
edit_button = sg.Button(dict.edit_button)
complete_button = sg.Button(dict.complete_button)
mark_completed_button = sg.Button(dict.mark_button)
label_select = sg.Text(key="select", text_color="red")

remove_button = sg.Button(dict.remove_button)

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
            input_box = sg.InputText(tooltip=dict.enter, key="todo")
            label = sg.Text(dict.todo_prompt)
            layout = [[clock],
                      [label],
                      [input_box, add_button],
                      [label_select],
                      [list_box, edit_button, complete_button],
                      [remove_button, exit_button]]
        else:
            input_box = sg.InputText(tooltip=dict.enter, key="todo", readonly=True)
            label = sg.Text(dict.viewer_mode_msg)
            layout = [[clock],
                      [label],
                      [input_box, mark_completed_button],
                      [label_select],
                      [list_box],
                      [exit_button]]
    case "Exit" | sg.WIN_CLOSED:
        exit("Bye")
window0.close()

window = sg.Window(dict.editor_head,
                   layout=layout,
                   font=('GeorgiaPro', 20))
while True:
    event, values = window.read(timeout=200)
    window['clock'].update(value="Today is " + time.strftime("%A, %B %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todolist = get_todos()
            new_todo = "add " + values['todo']
            tdf.todolist_add(todolist, new_todo)
            window['todos'].update(values=todolist)
        case "Edit":
            try:
                new_todo = values['todo'].capitalize() + '\n'
                todolist = get_todos()
                indexes = list_box.get_indexes()
                index = indexes[0]
                todolist[index] = new_todo
                write_todos(todolist)
                window['todos'].update(values=todolist)
            except IndexError:
                window["select"].update(value=dict.select_msg)
                # another option: sg.popup(dict.select_msg, font=('GeorgiaPro', 20))
                continue
        case "Complete":
            try:
                todolist = get_todos()
                indexes = list_box.get_indexes()
                index = indexes[0]
                todolist.pop(index)
                write_todos(todolist)
                window['todos'].update(values=todolist)
                window['todo'].update(value='')
            except IndexError:
                window["select"].update(value=dict.select_msg)
                # another option: sg.popup(dict.select_msg, font=('GeorgiaPro', 20))
                continue
        case "Mark as completed":
            try:
                new_todo = values['todo'].capitalize() + ' - COMPLETED\n'
                todolist = get_todos()
                indexes = list_box.get_indexes()
                index = indexes[0]
                if '- COMPLETED' not in todolist[index]:
                    todolist[index] = new_todo
                write_todos(todolist)
                window['todos'].update(values=todolist)
                window['todo'].update(value='')
            except IndexError:
                window["select"].update(value=dict.select_msg)
                # another option: sg.popup(dict.select_msg, font=('GeorgiaPro', 20))
                continue
        case 'Remove completed':
            todolist = get_todos()
            for t in todolist:
                if '- COMPLETED' in t:
                    todolist.remove(t)
                    write_todos(todolist)
            window['todos'].update(values=todolist)
        case 'todos':
            window["select"].update(value="")
            window['todo'].update(value=values['todos'][0].strip('\n'))
        case "Exit" | sg.WIN_CLOSED:
            break
print("Bye")
window.close()
