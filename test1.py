import streamlit as st
import numpy as np
from dotenv import load_dotenv
import google.genai as genai
import os 


load_dotenv(dotenv_path=".env")
gemini_api_key = os.getenv("GENAI_API_KEY")
client = genai.Client(api_key=gemini_api_key)
@st.cache_data

def long_running_function():
    kermit = "https://tenor.com/en-GB/view/kermit-falling-building-fall-woodz-gif-24715383.gif"
    return kermit 

long_running_function()
st.header("hello wroldl")
st.button("click meEE", type = "primary")

if st.button("click me", type="primary"):
    st.text("you beat uo children!")
gayness = st.select_slider(label = "how pride are you", options = ["straight", "gay", "lesbian", "asexual", "bisexual", "pansexual"])
if gayness != "straight":
    st.header("happy pride month you werirdo")


goal = st.text_input("your meesgae")
skibidi = st.slider(min_value=0, max_value = 100, value = 50, label="skibidi")
st.text(f"Your goal is: {goal}")

st.image(long_running_function(), caption="kermit falling", width=300)

st.chat_message("user").title("hi im adithya im short")
st.chat_message("assistant").text("hi hi im adithya im short")
st.chat_message("user").text("wahts ur name sir")
if user_input:= st.chat_input(placeholder="type your message here"):
    st.chat_message("user").text(user_input)
  
response = client.models.generate_content(
    model = "gemini-2.0-flash",
    contents = user_input
)
st.chat_message("ai").text(response.text)