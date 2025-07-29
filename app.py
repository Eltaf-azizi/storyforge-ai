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
            data = response.json()
            story_text = data["story"]
            audio_url = data["audion_url"]


            # Display Story
            st.subheader("Your AI-Generated Story")
            st.write(story_text)



            # Play Audio
            st.subheader("Listen to Your Story")
            st.audio(audio_url)
            



            # Download Story as TXT
            story_file = f"story_{genre}_{theme}.txt"
            with open(story_file, "w", encoding="utf-8") as f:
                f.write(story_text)


            
            st.download_button(label="Download Story as Text", data=story_text, file_name=story_file, mime="text/plain")


        else:
            st.error("Error generating the story. Please try again.")
            