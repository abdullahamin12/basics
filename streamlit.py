import streamlit as st 
import requests
URL="http://127.0.0.1:8000"
st.title("Todo App")
st.write("Connected to fastapi backend")

with   st.form("Todo form "):
    title=st.text_input("Add todo title")
    done=st.checkbox("done")
    submited=st.form_submit_button("add todo")
    if submited:
        st.write("TItle:",title)
        st.write("DONE:",done)

responce=requests.get(f"{URL}/todos/")
if responce.status_code==200:
    todos=responce.json()
    st.subheader("All todos")
    st.json(todos)
    
else:
    print("error")