from datetime import datetime

from pydantic import BaseModel, Field, model_validator


class TodoCreate(BaseModel):
    title: str = Field(min_length=1, max_length=200)
    completed: bool = False


class TodoUpdate(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=200)
    completed: bool | None = None

    @model_validator(mode="after")
    def reject_explicit_nulls(self):
        for field_name in self.model_fields_set:
            if getattr(self, field_name) is None:
                raise ValueError(f"'{field_name}' must not be null")
        return self


class TodoResponse(BaseModel):
    id: int
    title: str
    completed: bool
    created_at: datetime
    updated_at: datetime

    model_config = {"from_attributes": True}
