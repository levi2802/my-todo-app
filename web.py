import streamlit as st
import functions

todos = functions.get_todos()
# Helps to adjust the screen size to fit the device.
st.set_page_config(layout='wide')

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo)
    functions.write_todos(todos)


st.title("My ToDo App")
st.subheader("This is my todo app")
# Default unsafe_allow_html is set to false, so html tags will not be activated.
st.write("This app is to increase my <b>productivity</b>", unsafe_allow_html=True)


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)

    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add new todo",
              on_change=add_todo, key='new_todo')
