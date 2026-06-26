import streamlit as st 
import requests
URL="http://127.0.0.1:8000"
st.title("Todo App")
st.write("Connected to fastapi backend")
with  st.form("Todo form "):
    title=st.text_input("Add todo title")
    done=st.checkbox("done")
    submited1=st.form_submit_button("add todo")
    if submited1:
        pay_load={"title":title,"done":done}
        st.write(pay_load)
        responce=requests.post(f"{URL}/todos/",json=pay_load)
        if responce.status_code==200:
           st.success("Todo Added")
           st.rerun()
        else:
           print("error")
with st.form("DELETE TODO FORM"):

    delete_id = st.text_input("which to del")
    disclaimer = st.checkbox("really do you wanna delete")
    delete_clicked = st.form_submit_button("delete permanently")

    if delete_clicked:
        if disclaimer:
            if delete_id.isdigit():
                response = requests.delete(f"{URL}/todos/{int(delete_id)}")
                if response.status_code == 200:
                    st.success("Todo deleted")
                    st.rerun()
                else:
                    st.error("Delete failed")
            else:
                st.error("Enter a valid number")
        else:
            st.warning("Please tick the checkbox")

responce=requests.get(f"{URL}/todos/")
if responce.status_code==200:
    todos=responce.json()
    st.subheader("All todos")
    st.json(todos)
    
else:
    print("error")

