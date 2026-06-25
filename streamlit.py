import streamlit as st 
import requests
URL="http://127.0.0.1:8000"
st.title("Todo App")
st.write("Connected to fastapi backend")
responce=requests.get(f"{URL}/todos/")
if responce.status_code==200:
    todos=responce.json()
    st.subheader("All todos")
    st.json(todos)
    
else:
    print("error")