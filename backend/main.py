from fastapi import FastAPI
from routers import tasks, users
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise


app = FastAPI()

app.include_router(tasks.router)
app.include_router(users.router)


origins = [
    "http://localhost:5173"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
)

register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["routers.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)