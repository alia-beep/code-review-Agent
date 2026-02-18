import time
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

client = OpenAI(
    base_url=os.getenv("SCALEDOWN_API_URL"),
    api_key=os.getenv("GITHUB_TOKEN")
)

class CodeInput(BaseModel):
    code: str

@app.post("/review")
async def review_code(input: CodeInput):
    start_time = time.time()
    try:
        response = client.chat.completions.create(
            
            messages=[
                { "role": "system", "content": "You are a code reviewer. Give exactly 3 points. 1. Start bugs with 'ERROR:'. 2. Start suggestions with 'TIP:'. 3. DO NOT use markdown code blocks (```) or bold symbols (**). Keep it as plain text only."
                },
                {"role": "user", "content": input.code}
                ],
            model="gpt-4o"
        )
        ai_msg = response.choices[0].message.content
        runtime_ms = round((time.time() - start_time) * 1000, 2)

        return {
            "status": "success",
            "runtime": f"{runtime_ms} ms",
            "full_review": ai_msg.split("\n")
        }
    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)