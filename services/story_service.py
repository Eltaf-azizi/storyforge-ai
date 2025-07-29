import openai
import os
from dotenv import load_dotenv
from ggts import gTTS
import uuid


# Load envirnoment 
load_dotenv()



# get api key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


client = openai.OpenAI(api_key = OPENAI_API_KEY)



def generate_ai_story(genre: str, theme: str, length: str):
    prompt = f"write a {length} {genre} story about {theme}. Make it engaging and creative"


    response = client.chat.completions.create(
        model="gpt-turbo-3.5",
        messages=[
            {"role": "system", "content": "you are a creative storyteller"},
            {"role": "user", "content": prompt}
        ],
        max_token=500
    )


    story = response.choices[0].message.content
    return 




def text_to_speech(story_text):
    tts = gTTS(text=story_text, lang="en")
    filename = f"story_{uuid.uuid4().hex}.mp3"
    file_path = f"static/{filename}"
    tts.save(file_path)


    return file_path
