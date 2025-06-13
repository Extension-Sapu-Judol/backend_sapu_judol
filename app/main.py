from fastapi import FastAPI
import os
from dotenv import load_dotenv
from typing import List
from app.schemas.Comment import Comment
from app.database.db import supabase
from app.lib.model_sapu_judol import predict_comment

load_dotenv()

app = FastAPI()

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
