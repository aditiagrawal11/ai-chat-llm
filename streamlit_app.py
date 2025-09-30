import streamlit as st
from app.chat_interface import get_response

st.title("AI Chat LLM 🤖")
user_input = st.text_input("You:", "")
if user_input:
    response = get_response(user_input)
    st.write("Bot:", response)
