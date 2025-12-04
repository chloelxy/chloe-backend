from fastapi import FastAPI
from pydantic import BaseModel
import cohere
import os
from dotenv import load_dotenv

load_dotenv()

class chatRequest(BaseModel):
    prompt: str

class chatResponse(BaseModel):
    response: str

app = FastAPI()
cohere_client = cohere.ClientV2(api_key=os.getenv("COHERE_API_KEY"))

@app.get("/")
def calculation():
    answer = 10 + 10
    return {"answer": answer}

@app.post("/chat", response_model=chatResponse)
def chat(request: chatRequest):
    response = cohere_client.chat(
        model="command-a-03-2025",
        messages=[
            {
                "role": "user",
                "content": request.prompt
            }
        ]
    )

    print(response)
    return chatResponse(response=f"Hi, how are you!")