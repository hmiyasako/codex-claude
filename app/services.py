from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models import Todo
from app.schemas import TodoCreate, TodoUpdate


def create_todo(db: Session, data: TodoCreate) -> Todo:
    todo = Todo(title=data.title, completed=data.completed)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


def list_todos(db: Session) -> list[Todo]:
    return db.query(Todo).all()


def get_todo(db: Session, todo_id: int) -> Todo | None:
    return db.query(Todo).filter(Todo.id == todo_id).first()


def update_todo(db: Session, todo: Todo, data: TodoUpdate) -> Todo:
    update_data = data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(todo, field, value)
    todo.updated_at = datetime.now(timezone.utc)
    db.commit()
    db.refresh(todo)
    return todo


def delete_todo(db: Session, todo: Todo) -> None:
    db.delete(todo)
    db.commit()
