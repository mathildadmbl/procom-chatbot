from fastapi import FastAPI, Request
import openai
from transformers import pipeline

from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()
openai.api_key = os.getenv("OPENAI_API_KEY")


