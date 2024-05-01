import streamlit as st
from modules import dict, file_functions as ff

todolist = ff.get_todos()

st.title("My Todo App")
st.subheader("My Todo App, just smaller")
st.write("And with teeny tiny letters for people with good eyes!!!")

for index, item in enumerate(todolist):
    st.checkbox(item, key=index)

st.text_input(label="", placeholder=dict.todo_prompt)
