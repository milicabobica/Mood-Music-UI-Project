from huggingface_hub import InferenceClient
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

load_dotenv()

repo_id = "openai/gpt-oss-120b"
hf_token = os.getenv("HF_TOKEN")
if not hf_token:
    raise ValueError("HF_TOKEN environment variable not set!")

llm_client = InferenceClient(
    model=repo_id,
    timeout=120,
    token=hf_token
)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate")
async def generate(request: Request):
    data = await request.json()
    emotion = data.get("emotion", "")

    prompt = f"""
        I want a music playlist of songs that best describe the '{emotion}'.
        Each song should be returned in a numbered list:
        1. Song Title – Artist – Year
        2. ...
        3. ...
        Ensure the output is correctly formatted.
    """
    try:
        response = llm_client.chat_completion(
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        print("DEBUG raw response:", response)

        # safely extract content
        content = ""
        if hasattr(response, "choices") and len(response.choices) > 0:
            content = response.choices[0].message.get("content", "")
        else:
            content = str(response)

        return {"playlist": content}

    except Exception as e:
        print("ERROR:", e)
        return {"error": str(e)}
