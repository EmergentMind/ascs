from app.core.database import get_session

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware

from sqlmodel import Session 
from typing import Annotated

from app.api.main import api_router 

app = FastAPI()

origins = [
        "http://localhost",
        "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods = ["*"],
    allow_headers= ["*"],
        )

app.include_router(api_router)
