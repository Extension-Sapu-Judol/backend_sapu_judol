from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv
from typing import List
from app.schemas.Comment import Comment
from app.database.db import supabase
from app.lib.model_sapu_judol import predict_comment

load_dotenv()

app = FastAPI()

# Daftar origin yang diperbolehkan (frontend, tools, dll)
origins = [
    "http://localhost:3000",       # misalnya frontend Next.js lokal
    "http://127.0.0.1:3000",
    "https://your-frontend.com",
    'https://www.youtube.com' 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,            # Atau ["*"] untuk semua origin (tidak direkomendasikan untuk production)
    allow_credentials=True,
    allow_methods=["*"],              # Atau daftar seperti ["GET", "POST"]
    allow_headers=["*"],              # Header yang diizinkan
)

@app.get("/")
def read_root():
  return {"message": "Hello from FastAPI"}

@app.post("/filter_comments")
def filter_comments(comments: List[Comment]):
  result = []
  for comment in comments:
    result.append({
      "id": comment.id,
      "text": comment.text,
      "is_judol": predict_comment(comment.text)
    })

  return {"comments": result}

# @app.get("/env")
# def get_env():
  # return {"your_env_variable": os.getenv("YOUR_ENV_VAR", "Not Set")}
