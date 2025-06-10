import streamlit as st
import numpy as np
from dotenv import load_dotenv
import google.genai as genai
import os 


load_dotenv(dotenv_path=".env")
gemini_api_key = os.getenv("GENAI_API_KEY")
client = genai.Client(api_key=gemini_api_key)

st.header("ai tutor cuz i lazy")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [["ai", "hi im ur tutor ask me anything"]]

for role, message in st.session_state.chat_history:
    st.chat_message(role).markdown(message)

user_input = st.chat_input(placeholder="type your message here", key ="user_input")

if user_input:
    st.chat_message("user").text(user_input)
    st.session_state.chat_history.append(["user", user_input])
    
    response = client.models.generate_content(
        model = "gemini-2.0-flash",
        config= genai.types.GenerateContentConfig(system_instruction="You are a helpful tutor. Answer the user's questions in a friendly and informative manner."),
        contents = st.session_state.chat_history
    )
    ai_response = response.text
    st.chat_message("ai").text(ai_response)
    st.session_state.chat_history.append(["ai", ai_response])
    


