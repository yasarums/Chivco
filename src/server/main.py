import uvicorn
from fastapi import FastAPI
from routes.reservation import router as reservation_router
from routes.appointment import router as appointment_router
from routes.progrep import router as progrep_router

app = FastAPI()

app.include_router(reservation_router, prefix = "/reservations")
app.include_router(appointment_router, prefix = "/appointments")
app.include_router(progrep_router, prefix = "/progreps")