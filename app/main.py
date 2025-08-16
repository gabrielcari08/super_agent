from fastapi import FastAPI
from app.routers import user, auth, tasks

app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
async def hello_fastapi():
    return {"message": "Hello FastAPI !"}