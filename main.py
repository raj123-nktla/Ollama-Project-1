from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"

class ProfileInput(BaseModel):
    profile_text: str

def generate_text(prompt: str):
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        }
    )
    return response.json()["response"]

@app.post("/generate")
def generate_outreach(data: ProfileInput):
    profile = data.profile_text

    email_prompt = f"""
You are writing a FIRST cold email.

Person profile:
{profile}

Write a personalized cold email (90-150 words).
Tone: professional and friendly.
End with a clear CTA.
"""

    linkedin_prompt = f"""
You are writing a FIRST LinkedIn DM.

Person profile:
{profile}

Write a short, casual LinkedIn DM (40-80 words) .
Avoid salesy language.
"""

    email = generate_text(email_prompt)
    linkedin = generate_text(linkedin_prompt)

    return {
        "email": email,
        "linkedin_dm": linkedin
    }
