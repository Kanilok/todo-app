from typing import List
from .models import Task_Pydantic, User_Pydantic, Tasks, Users
from .users import get_current_user
from pydantic import BaseModel
from tortoise.contrib.fastapi import HTTPNotFoundError
from fastapi import APIRouter, HTTPException, Depends
from datetime import date



router = APIRouter(
    prefix = "/tasks",
    tags = ["tasks"]
)


@router.get("/", response_model=List[Task_Pydantic])
async def get_unarchived_tasks(user: User_Pydantic = Depends(get_current_user)):
    user_id = user.dict()["id"]
    user1 = await Users.get(id=user_id)
    return await Task_Pydantic.from_queryset(Tasks.filter(user = user1, archived=False))

@router.get("/archived", response_model=List[Task_Pydantic])
async def get_archived_tasks():
    return await Task_Pydantic.from_queryset(Tasks.filter(archived=True))


@router.post("/", response_model=Task_Pydantic)
async def create_task(task: str, date: str, user: User_Pydantic = Depends(get_current_user)):
    user_id = user.dict()["id"]
    user1 = await Users.get(id=user_id)
    task_obj = await Tasks.create(description=task, due_date=date, user = user1)
    return await Task_Pydantic.from_tortoise_orm(task_obj)


@router.put(
    "/is-done/{task_id}", response_model=Task_Pydantic, responses={404: {"model": HTTPNotFoundError}}
)
async def update_status(task_id: int, is_late: bool):
    is_done = await Task_Pydantic.from_queryset_single(Tasks.get(id=task_id))
    await Tasks.filter(id=task_id).update(is_done = not is_done.dict()["is_done"])
    if not is_done.dict()["is_done"]:
        await Tasks.filter(id=task_id).update(done_date = date.today())
        await Tasks.filter(id=task_id).update(done_on_time = not is_late)
    else:
        await Tasks.filter(id=task_id).update(done_date = None)
        await Tasks.filter(id=task_id).update(done_on_time = None)
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
