from pydantic import BaseModel, Field
from datetime import datetime

from ...repository.utils import IPost

class BasePostSchema(BaseModel, IPost):
    title: str = Field(..., min_length=1, max_length=100)
    content: str = Field(..., min_length=1)

    def dict(self):
        return self.model_dump(exclude_unset=True)

class PostResponseSchema(BasePostSchema):
    created_at: datetime

    class Config:
        from_attributes = True
#post update schema

class PostUpdateSchema(BasePostSchema):
    title: str | None = Field(default=None, min_length=1, max_length=100) 
    content: str | None = Field(default=None, min_length=1) 


