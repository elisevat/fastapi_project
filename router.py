from typing import Annotated

from fastapi import APIRouter, Depends

from repository import TaskRepository
from schemas import STaskAdd, STaskGet, STaskId

router = APIRouter(
    prefix='/tasks',
    tags=["Таски"],
)


@router.get("")
async def get_tasks() -> list[STaskGet]:
    tasks = await TaskRepository.get_tasks()
    return tasks


@router.post("")
async def add_task(
        task: Annotated[STaskAdd, Depends()],
) -> STaskId:
    task_id = await TaskRepository.add_task(task)
    return {'ok': True, 'task_id': task_id}