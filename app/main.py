from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas.request import CareerQuery

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "AI Career Agent is running"}

@app.post("/suggest")
def suggest_career(query: CareerQuery):
    result = run_career_agent(query.interests)
    return result 