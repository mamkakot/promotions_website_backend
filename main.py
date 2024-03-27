from contextlib import asynccontextmanager

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing_extensions import Annotated

from database import create_tables
from repository import Repository
from shemas import CardNumberInfo


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    print('Database is ready')
    yield
    # await delete_tables()
    print("Database is cleared")


app = FastAPI(lifespan=lifespan, title="alley_promotions")

origins = [
    "http://localhost:3000",
    "https://фитнес-аллея.рф",
    "https://аллея-фитнес.рф",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=["Content-Type", "Access-Control-Allow-Headers", "Access-Control-Allow-Origin"],
)


@app.get('/winners')
async def get_winners():
    return await Repository.get_winners()


@app.post('/card_numbers')
async def add_card_number(card_number: Annotated[CardNumberInfo, Depends()]):
    card_number_id = await Repository.add_card_number(card_number)
    return {"ok": True, "card_number_id": card_number_id}
