from modules import dict, todolist_functions as tdf
from modules.file_functions import get_todos
import PySimpleGUI as sg

label = sg.Text("Type in an todo: ")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window("To-Do List: Editor mode", layout=[[label, input_box], [add_button]])
window.read()
window.close()
