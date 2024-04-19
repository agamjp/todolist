from modules import dict, todolist_functions as tdf
from modules.file_functions import get_todos, write_todos
import PySimpleGUI as sg

label = sg.Text(dict.todo_prompt)
input_box = sg.InputText(tooltip=dict.enter, key="todo")
add_button = sg.Button(dict.add_button)

list_box = sg.Listbox(values=get_todos(), key='todos',
                      enable_events=True, size=(45, 10))
edit_button = sg.Button(dict.edit_button)

exit_button = sg.Button(dict.exit_button)

window = sg.Window(dict.editor_head,
                   layout=[[label], [input_box, add_button],
                           [list_box, edit_button],
                           [exit_button]],
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
        case "Exit"|sg.WIN_CLOSED:
            break

window.close()
