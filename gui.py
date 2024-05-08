from modules import dict
from modules.file_functions import get_todos, write_todos, resource_path
import PySimpleGUI as sg
import time
import os
from dotenv import load_dotenv

load_dotenv()

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("BluePurple")

label0 = sg.Text(dict.password_prompt)
input_box0 = sg.InputText(tooltip=dict.password, key="password", password_char='*')
enter_button = sg.Button(dict.enter_button)

clock = sg.Text('', key='clock')
add_button = sg.Button(key=dict.add_button, size=3, image_source=resource_path("add.png"),
                       button_color=sg.theme_background_color(), tooltip="Add Todo")

list_box = sg.Listbox(values=get_todos(), key='todos', enable_events=True, size=(45, 10))
edit_button = sg.Button(dict.edit_button)
complete_button = sg.Button(dict.complete_button)
mark_completed_button = sg.Button(key=dict.mark_button, size=3, image_source=resource_path("complete.png"),
                                  button_color=sg.theme_background_color(),
                                  tooltip="Mark as completed")
label_select = sg.Text(key="select", text_color="red")

remove_button = sg.Button(dict.remove_button)
# change_password_button = sg.Button(dict.change_pswrd_button)

exit_button0 = sg.Button(dict.exit_button)
exit_button = sg.Button(dict.exit_button)

if os.getenv("PASSWORD") is not None:
    window0 = sg.Window(dict.editor_head,
                        layout=[[label0], [input_box0, enter_button],
                                [exit_button0]],
                        font=('GeorgiaPro', 20))
    event, values = window0.read()
    layout = []
    password = os.getenv("PASSWORD")
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
                # add change_password_button when ready
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
else:
    input_box = sg.InputText(tooltip=dict.enter, key="todo")
    label = sg.Text(dict.todo_prompt)
    layout = [[clock],
              [label],
              [input_box, add_button],
              [label_select],
              [list_box, edit_button, complete_button],
              [remove_button, exit_button]]

window = sg.Window(dict.editor_head,
                   layout=layout,
                   font=('GeorgiaPro', 20))
while True:
    event, values = window.read(timeout=200)
    print(event, values)
    if values is not None:
        window['clock'].update(value="Today is " + time.strftime("%A, %B %d, %Y %H:%M:%S"))
        match event:
            case "Add":
                todolist = get_todos()
                if values['todo'] == "":
                    sg.popup(dict.no_empty_msg)
                    # chores = get_todos("chores.txt") - won't work in .exe
                    # new_todo = random.choice(chores) + '\n'
                else:
                    new_todo = values['todo'].capitalize() + '\n'
                    todolist.append(new_todo)
                write_todos(todolist)
                window['todos'].update(values=todolist)
            case "Edit":
                try:
                    new_todo = values['todo'].capitalize() + '\n'
                    todolist = get_todos()
                    indexes = list_box.get_indexes()
                    index = indexes[0]
                    if new_todo != "\n":
                        todolist[index] = new_todo
                    else:
                        sg.popup(dict.no_empty_msg)
                    write_todos(todolist)
                    window['todos'].update(values=todolist)
                except IndexError:
                    window["select"].update(value=dict.select_msg)
                    # another option: sg.popup(dict.select_msg, font=('GeorgiaPro', 20)
                    # (also for Complete/Mark as completed)
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
                    continue
            case 'Remove completed':
                todolist = get_todos()
                to_remove = []
                for t in todolist:
                    if '- COMPLETED' in t:
                        to_remove.append(t)
                for i in to_remove:
                    todolist.remove(i)
                write_todos(todolist)
                window['todos'].update(values=todolist)
            # case "Change password":
                # password_setter.set_password()
        # needs debugging (change password window opens only once)
            case 'todos':
                window["select"].update(value="")
                try:
                    window['todo'].update(value=values['todos'][0].strip('\n'))
                except IndexError:
                    sg.popup(dict.no_todos_msg)
            case "Exit" | sg.WIN_CLOSED:
                break
    else:
        break
print("Bye")
window.close()
