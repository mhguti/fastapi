from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from . import models, config
from .database import engine

from .routers import post,user, auth, vote
from fastapi.middleware.cors import CORSMiddleware


#since alembic, no longer needed - models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

""" while True:
    try:
        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='password123', cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("Database connection was successful")
        break
    except Exception as error:
        print("Connecting to database failed")
        print("Error: ", error)
        time.sleep(3) """


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)






@app.get("/", tags=['Hello World'], summary="Hello World API")
def read_root():
    return {"message": "Hi There"}


