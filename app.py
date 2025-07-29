import streamlit as st
import requests


# FastAPI endpoint
API_URL = "http://127.0.0.1:8000/generate_story"


# Streamlit UI
st.title("AI-Powered Creative Story Generator")
st.write("Generate unique AI-powered stories and listen to them!")