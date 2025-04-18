import streamlit as st
import requests
import os

# Load API key from environment
API_KEY = os.getenv("HUGGINGFACE_API_KEY")
API_URL = "https://api-inference.huggingface.co/models/facebook/opt-350m"

def generate_text(prompt):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    return response.json()

st.title("🚀 Space AI Text Generator")
user_input = st.text_input("Enter your mission prompt:")
if st.button("Generate Response"):
    result = generate_text(user_input)
    st.write(result)