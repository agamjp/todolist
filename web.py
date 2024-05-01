import streamlit as st
from modules import dict, file_functions as ff


todolist = ff.get_todos()
def add_todo(todos=todolist):
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    ff.write_todos(todos)
    st.session_state["new_todo"] = ''


st.title("My Todo App title")
st.subheader("My Todo App title, just smaller")
st.write("And with teeny tiny letters for people with good eyes!!!")

for index, item in enumerate(todolist):
    checkbox = st.checkbox(item, key=index)
    if checkbox:
        print(checkbox)
        print(item)
        todolist.pop(index)
        ff.write_todos(todolist)
        del st.session_state[index]
        st.rerun()

st.text_input(label="", placeholder=dict.todo_prompt,
              key="new_todo", on_change=add_todo)
