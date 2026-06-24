from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from prompt import build_prompt
from service import generate_plan

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TravelRequest(BaseModel):
    destination: str
    days: int
    people: int
    budget: str
    style: str
    must_go: str = ""

@app.post("/generate")
def create_plan(req: TravelRequest):
    prompt = build_prompt(req.dict())
    result = generate_plan(prompt)
    return {"result": result}