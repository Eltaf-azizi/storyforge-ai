import openai
import os
from dotenv import load_dotenv
from ggts import gTTS
import uuid


# Load envirnoment 
load_dotenv()



# get api key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")