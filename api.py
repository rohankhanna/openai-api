from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import openai
from dotenv import load_dotenv
load_dotenv()

# Initialize OpenAI client with the new SDK (>=1.0.0)
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

class PromptInput(BaseModel):
    prompt: str

@app.post("/ask-openai")
async def ask_openai(data: PromptInput):
    try:
        response = client.chat.completions.create(
            model="gpt-4",  # or "gpt-3.5-turbo"
            messages=[
                {"role": "user", "content": data.prompt}
            ]
        )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
