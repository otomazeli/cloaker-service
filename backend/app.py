from fastapi import FastAPI, Depends, HTTPException
from routes import router
from database import get_db

app = FastAPI(title="Cloaker & Bot Detection API")

@app.on_event("startup")
def startup_event():
    get_db()


app.include_router(router)