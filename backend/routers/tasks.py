from typing import List, Union
from .models import Task_Pydantic, TaskIn_Pydantic, User_Pydantic, Tasks, Users
from .users import get_current_user
from tortoise.contrib.fastapi import HTTPNotFoundError
from fastapi import APIRouter, Depends
from datetime import date

router = APIRouter(
    prefix = "/tasks",
    tags = ["tasks"]
)


@router.get("/", response_model=List[Task_Pydantic])
async def get_unarchived_tasks(user: User_Pydantic = Depends(get_current_user)):
    user_id = user.dict()["id"]
    user_model = await Users.get(id=user_id)
    return await Task_Pydantic.from_queryset(Tasks.filter(user = user_model, archived=False))


@router.post("/", response_model=Task_Pydantic)
async def create_task(task: TaskIn_Pydantic, user: User_Pydantic = Depends(get_current_user)):
    user_id = user.dict()["id"]
    user_model = await Users.get(id=user_id)
    task_obj = await Tasks.create(task_name = task.task_name, due_date = task.due_date, description = task.description, user = user_model)
    return await Task_Pydantic.from_tortoise_orm(task_obj)


@router.put(
    "/{task_id}", response_model=Task_Pydantic, responses={404: {"model": HTTPNotFoundError}}
)
async def update_status(task_id: int, task: TaskIn_Pydantic, user: User_Pydantic = Depends(get_current_user)):
    await Tasks.filter(id=task_id).update(task_name = task.task_name, due_date = task.due_date, description = task.description)
    return await Task_Pydantic.from_queryset_single(Tasks.get(id=task_id))


@router.put(
    "/is-done/{task_id}", response_model=Task_Pydantic, responses={404: {"model": HTTPNotFoundError}}
)
async def update_status(task_id: int, task: TaskIn_Pydantic, user: User_Pydantic = Depends(get_current_user)):
    is_done = await Task_Pydantic.from_queryset_single(Tasks.get(id=task_id))
    await Tasks.filter(id=task_id).update(is_done = not is_done.dict()["is_done"])
    if not is_done.dict()["is_done"]:
        await Tasks.filter(id=task_id).update(done_date = date.today())
        await Tasks.filter(id=task_id).update(done_on_time = task.done_on_time)
    else:
        await Tasks.filter(id=task_id).update(done_date = None)
        await Tasks.filter(id=task_id).update(done_on_time = None)
    return await Task_Pydantic.from_queryset_single(Tasks.get(id=task_id))

@router.put(
    "/archived/{task_id}", response_model=Task_Pydantic, responses={404: {"model": HTTPNotFoundError}}
)
async def update_archive(task_id: int, user: User_Pydantic = Depends(get_current_user)):
    archived = await Task_Pydantic.from_queryset_single(Tasks.get(id=task_id))
    await Tasks.filter(id=task_id).update(archived = not archived.dict()["archived"])
    return await Task_Pydantic.from_queryset_single(Tasks.get(id=task_id))

