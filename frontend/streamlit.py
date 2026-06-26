import streamlit as st
import requests
import pandas as pd

URL = "http://backend:8000"

st.title("Todo App")
st.write("Connected to FastAPI backend")

with st.form("add_todo_form"):
    title = st.text_input("Add todo title")
    done = st.checkbox("Done")
    add_clicked = st.form_submit_button("Add todo")

    if add_clicked:
        payload = {"title": title, "done": done}
        response = requests.post(f"{URL}/todos/", json=payload)
        if response.status_code == 200:
            st.success("Todo added")
            st.rerun()
        else:
            st.error("Error adding todo")

with st.form("delete_todo_form"):
    delete_id = st.text_input("Todo ID to delete")
    confirm_delete = st.checkbox("Really delete this todo")
    delete_clicked = st.form_submit_button("Delete permanently")

    if delete_clicked:
        if not confirm_delete:
            st.warning("Please tick the checkbox")
        elif not delete_id.isdigit():
            st.error("Enter a valid number")
        else:
            response = requests.delete(f"{URL}/todos/{int(delete_id)}")
            if response.status_code == 200:
                st.success("Todo deleted")
                st.rerun()
            else:
                st.error("Delete failed")

with st.form("update_todo_form"):
    update_id = st.text_input("Todo ID to update")
    new_title = st.text_input("New todo title")
    new_done = st.checkbox("Done")
    update_clicked = st.form_submit_button("Update todo")

    if update_clicked:
        if not update_id.isdigit():
            st.error("Enter a valid number")
        else:
            payload = {"title": new_title, "done": new_done}
            response = requests.put(f"{URL}/todos/{int(update_id)}", json=payload)
            if response.status_code == 200:
                st.success("Todo updated")
                st.rerun()
            else:
                st.error("Update failed")

response = requests.get(f"{URL}/todos/")
if response.status_code == 200:
    todos = response.json()
    st.subheader("All todos")
    df = pd.DataFrame(todos)
    st.dataframe(df)
else:
    st.error("Error loading todos")