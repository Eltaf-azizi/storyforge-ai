import streamlit as st
import requests


# FastAPI endpoint
API_URL = "http://127.0.0.1:8000/generate_story"


# Streamlit UI
st.title("AI-Powered Creative Story Generator")
st.write("Generate unique AI-powered stories and listen to them!")


# User Inputs
genre = st.selectbox("Select Genre", ["Fantasy", "Sci-Fi", "Mystery", "Adventure", "Horror", "Romance"])
theme = st.text_input("Enter Story Theme", "A lost kingdom")
length = st.selectbox("Story Length", ["short", "medium", "long"])



# Generate Story Button
if st.button("Generate Story"):
    with st.spinner("Generating your story..."):
        response = requests.post(API_URL, json={"genre": genre, "theme": theme, "length": length})


        if response.status_code == 200:
            