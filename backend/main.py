from typing import List

from fastapi import FastAPI, HTTPException, Body
from models import Task_Pydantic, Tasks
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise


app = FastAPI()

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

class Status(BaseModel):
    message: str

class Task(BaseModel):
    task: str


@app.get("/tasks", response_model=List[Task_Pydantic])
async def index():
    return await Task_Pydantic.from_queryset(Tasks.all())


@app.post("/task", response_model=Task_Pydantic)
async def create_task(task: str):
    task_obj = await Tasks.create(description=task)
    return await Task_Pydantic.from_tortoise_orm(task_obj)


@app.put(
    "/task/{task_id}", response_model=Task_Pydantic, responses={404: {"model": HTTPNotFoundError}}
)
async def update_task(task_id: int):
    is_done = await Task_Pydantic.from_queryset_single(Tasks.get(id=task_id))
    await Tasks.filter(id=task_id).update(is_done = not is_done.dict()["is_done"])
    return await Task_Pydantic.from_queryset_single(Tasks.get(id=task_id))


@app.delete("/task/{task_id}", responses={404: {"model": HTTPNotFoundError}})
async def delete_task(task_id: int):
    deleted_count = await Tasks.filter(id=task_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    return Status(message=f"Deleted task {task_id}")


register_tortoise(
    app,
    db_url="sqlite://db.sqlite3",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)