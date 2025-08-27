from fastapi import FastAPI
from app.routers import user, auth, tasks, expenses
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(tasks.router)
app.include_router(expenses.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def hello_fastapi():
    return {"message": "Hello FastAPI !"}