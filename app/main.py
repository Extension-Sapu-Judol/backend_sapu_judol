# app/main.py
from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/")
def read_root():
  return {"message": "Hello from FastAPI"}

@app.get("/filter_comments")
def filter_comments():
  return "Filter Comments"

@app.get("/report")
def report():
  return "Report endpoint"

# @app.get("/env")
# def get_env():
  # return {"your_env_variable": os.getenv("YOUR_ENV_VAR", "Not Set")}
