from fastapi import APIRouter
from pydantic import BaseModel
from services.story_service import generate_ai_story, text_to_speech


router = APIRouter()


class storyRequest(BaseModel):
    genre: str
    theme: str
    length: str



@router.post("/generate_story")
def generate_story(request: StoryRequest):
    