from fastapi import FastAPI
import uvicorn
import os
import sys
from fastapi import Body
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from fastapi.responses import Response
from pydantic import BaseModel
from textSummarizer.pipeline.prediction import PredictionPipeline

text:str = "What is the Text Summarization?"

app = FastAPI()

app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train():
    try:
        os.system("python main.py")
        return Response(content="Training completed successfully!")

    except Exception as e:
        return Response(content=f"Error during training: {str(e)}")
    
    
class TextInput(BaseModel):
    text: str

pipeline_obj = PredictionPipeline()

@app.post("/predict")
async def predict(text: str = Body(..., media_type="text/plain")):
    result = pipeline_obj.predict(text)
    return {"summary": result}
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)    