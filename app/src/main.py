from fastapi import FastAPI, Form, File, UploadFile, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["OPTIONS", "GET", "POST"],
    allow_headers=["*"],
)

class User(BaseModel):
    age: int

def get_comic_preference(user: User):
    """Predict whether user prefers Marvel or DC movies"""
    if user.age > 20:
        return 'Marvel'
    else:
        return 'DC'

@app.get("/")
def root():
    return "healthy"

@app.post("/predict")
async def predict(user: User):
    comic_preference = get_comic_preference(user)
    return {
        "result": comic_preference,
        "error_code": 'everything_ok' 
    }
