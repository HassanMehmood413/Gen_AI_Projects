import google.generativeai as genai
import streamlit as st
import os

# Safely retrieve the API key

GOOGLE_API_KEY = 'AIzaSyAGO4moQfJYgS1bZ_9w_km0jm9ONufaOH8'

genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
# Initialize the model
def getResponseFromModel(user_input):
    try:
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit interface
st.set_page_config(page_title="Simple ChatBot", layout="centered")

# Title Name:
st.title("ChatGPT Pro")
st.write("Powered By Google Generative AI Gemini")

if 'history' not in st.session_state:
    st.session_state['history'] = []

# Display chat history
for user_message, bot_message in st.session_state.history:
    st.markdown(f"""
    <div style="
        background-color: black; 
        border-radius: 15px; 
        padding: 10px 15px; 
        margin: 5px 0; 
        max-width: 70%; 
        text-align: left; 
        display: inline-block;
    ">
        <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>You:</b> {user_message} 😊</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div style="
        background-color: grey; 
        color: white;
        border-radius: 15px; 
        padding: 10px 15px; 
        margin: 5px 0; 
        max-width: 70%; 
        text-align: left; 
        display: inline-block;
    ">
        <p style="margin: 0; font-size: 16px; line-height: 1.5;"><b>Bot:</b> {bot_message} 🤖</p>
    </div>
    """, unsafe_allow_html=True)

# Form for user input
with st.form(key='chatform', clear_on_submit=True):
    user_input = st.text_input('', max_chars=2000)
    submit_button = st.form_submit_button('Send')

    if submit_button:
        if user_input:
            response = getResponseFromModel(user_input)
            st.session_state.history.append((user_input, response))
        else:
            st.warning("Please enter a prompt.")

