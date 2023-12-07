import uvicorn
from fastapi import FastAPI
from routes.reservation import router as reservation_router

app = FastAPI()

app.include_router(reservation_router, prefix = "/reservations")