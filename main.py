from fastapi import FastAPI
from fastapi.staticfiles import staticfiles
from api.routes import router


app = FastAPI(title="AI-Powered Story Generator API")



app.include_router(router)


app.mount("/")
