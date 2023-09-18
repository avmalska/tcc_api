from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import main_router
from repository.mongo_database import MongoDatabase
from algorithms.kmeans import Kmeans


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(main_router)


@app.on_event("startup")
def on_startup():
    MongoDatabase.initialize()
    Kmeans.initialize()
