import streamlit as st
import google.generativeai as genai


st.title("Welcome To My Chatbot Intergated With Gemini Ai")

genai.configure(api_key="AIzaSyDlJCBdewTaJDdNajz2d2buZ6POa9uLpaE")

text = st.text_input("enter your question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])



if st.button("click me"):
   response = chat.send_message(text)
   st.write(response.text)