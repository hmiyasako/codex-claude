from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas import TodoCreate, TodoResponse, TodoUpdate
from app import services

router = APIRouter()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/todos", response_model=TodoResponse, status_code=201)
def create_todo(data: TodoCreate, db: Session = Depends(get_db)):
    return services.create_todo(db, data)


@router.get("/todos", response_model=list[TodoResponse])
def list_todos(db: Session = Depends(get_db)):
    return services.list_todos(db)


@router.get("/todos/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = services.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return todo


@router.patch("/todos/{todo_id}", response_model=TodoResponse)
def update_todo(todo_id: int, data: TodoUpdate, db: Session = Depends(get_db)):
    todo = services.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return services.update_todo(db, todo, data)


@router.delete("/todos/{todo_id}", status_code=204)
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = services.get_todo(db, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    services.delete_todo(db, todo)
