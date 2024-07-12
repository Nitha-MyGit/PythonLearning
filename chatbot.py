import streamlit as st
from streamlit import session_state
from streamlit import chat_message
from streamlit_chat import message
from utils import get_chatgpt_response,get_initial_message,update_chat

st.title("Chatbot : Using ChatGPT and Streamlit")
st.subheader("AI Programming Assistant")
model = st.selectbox(
    "Select your model",
    (
        "gpt-3.5-turbo",
        "gpt-4o"
    ),
)

if "generated" not in st.session_state:
    st.session_state["generated"]=[]

if "past" not in st.session_state:
    st.session_state["past"]=[]


#def clear_text():
#   st.session_state["input"]=""

query = st.text_input("Query:", key = "input")

if "messages" not in st.session_state:
    st.session_state["messages"] = (
        get_initial_message()
    )


if query:
    with st.spinner("generating response...."):
        messages = st.session_state["messages"]
        messages = update_chat(messages,"user",query)
        response = get_chatgpt_response(messages,model)
        messages = update_chat(messages,"assistant",response)
        st.session_state.past.append(query)
        st.session_state.generated.append(response)    
       

if st.session_state["generated"]:
    for i in range(len(st.session_state["generated"]) -1,-1,-1):
        message(st.session_state["past"][i], is_user = True, key = str(i) + "_user")
        message(st.session_state["generated"][i], key = str(i) + "_assistant")


with st.expander("show messages"):
    st.write(st.session_state["messages"])