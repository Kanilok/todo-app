from typing import List
from .models import Task_Pydantic, Tasks
from pydantic import BaseModel
from tortoise.contrib.fastapi import HTTPNotFoundError
from fastapi import APIRouter, HTTPException
from datetime import date


router = APIRouter(
    prefix = "/tasks",
    tags = ["tasks"]
)


class Status(BaseModel):
    message: str


@router.get("/", response_model=List[Task_Pydantic])
async def index():
    return await Task_Pydantic.from_queryset(Tasks.filter(archived=False))

@router.get("/archived", response_model=List[Task_Pydantic])
async def index():
    return await Task_Pydantic.from_queryset(Tasks.filter(archived=True))


@router.post("/", response_model=Task_Pydantic)
async def create_task(task: str, date: str):
    task_obj = await Tasks.create(description=task, due_date=date)
    return await Task_Pydantic.from_tortoise_orm(task_obj)


@router.put(
    "/is-done/{task_id}", response_model=Task_Pydantic, responses={404: {"model": HTTPNotFoundError}}
)
async def update_status(task_id: int):
    is_done = await Task_Pydantic.from_queryset_single(Tasks.get(id=task_id))
    await Tasks.filter(id=task_id).update(is_done = not is_done.dict()["is_done"])
    if is_done.dict()["is_done"]:
        Tasks.filter(id=task_id).update(done_date = date.today())
    else:
        Tasks.filter(id=task_id).update(done_date = None)
    return await Task_Pydantic.from_queryset_single(Tasks.get(id=task_id))

@router.put(
    "/archived/{task_id}", response_model=Task_Pydantic, responses={404: {"model": HTTPNotFoundError}}
)
async def update_archive(task_id: int):
    archived = await Task_Pydantic.from_queryset_single(Tasks.get(id=task_id))
    await Tasks.filter(id=task_id).update(archived = not archived.dict()["archived"])
    return await Task_Pydantic.from_queryset_single(Tasks.get(id=task_id))


@router.delete("/{task_id}", responses={404: {"model": HTTPNotFoundError}})
async def delete_task(task_id: int):
    deleted_count = await Tasks.filter(id=task_id).delete()
    if not deleted_count:
        raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
    return Status(message=f"Deleted task {task_id}")