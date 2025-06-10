import streamlit as st
import numpy as np
from dotenv import load_dotenv
import google.genai as genai
import os 


load_dotenv(dotenv_path=".env")
gemini_api_key = os.getenv("GENAI_API_KEY")
client = genai.Client(api_key=gemini_api_key)

def long_running_function():
    kermit = "https://tenor.com/en-GB/view/kermit-falling-building-fall-woodz-gif-24715383.gif"
    return kermit 

long_running_function()

def turnsfalse():
    st.session_state.clicked = False
# Initialize murders in session state if not already present
if "murders" not in st.session_state:
    st.session_state.murders = 0
    st.session_state.clicked = False
st.header("hello wroldl")
st.button("click meEE", type="primary", on_click=turnsfalse)

st.warning("⚠️ i warned you about this page :(")
# Display the metric at the desired position
if st.session_state.clicked == True:
    st.metric(label="murders", value=st.session_state.murders, delta=1, help="how many children you beat up")

def gimmedata():
    st.session_state.murders += 1

if st.button("click me", type="primary", on_click=gimmedata):
    st.text("you beat up children!")
    st.session_state.clicked = True 


gayness = st.select_slider(label = "how pride are you", options = ["straight", "gay", "lesbian", "asexual", "bisexual", "pansexual"])
if gayness != "straight":
    st.header("happy pride month you werirdo")


goal = st.text_input("your meesgae")
skibidi = st.slider(min_value=0, max_value = 100, value = 50, label="skibidi")
st.text(f"Your goal is: {goal}")


st.image(long_running_function(), caption="kermit falling", width=300)
st.header("ai tutor cuz i lazy")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [{"role": "ai", "message": "hi im ur tutor ask me anything"}]

for chat in st.session_state.chat_history:
    st.chat_message(chat["role"]).markdown(chat["message"])

user_input = st.chat_input(placeholder="type your message here", key="user_input")

if user_input:
    st.chat_message("user").text(user_input)
    st.session_state.chat_history.append({"role": "user", "message": user_input})
    
    formatted_history = [chat["message"] for chat in st.session_state.chat_history]

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=genai.types.GenerateContentConfig(system_instruction="You are a helpful tutor. Answer the user's questions in a friendly and informative manner."),
        contents=formatted_history
    )
    ai_response = response.text
    st.chat_message("ai").text(ai_response)
    st.session_state.chat_history.append({"role": "ai", "message": ai_response})



