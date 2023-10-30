from pydantic import BaseModel, Field


class PostSchema(BaseModel):
    title: str = Field(..., min_length=1, max_length=100)
    content: str = Field(..., min_length=1)

#post update schema

class PostUpdateSchema(BaseModel):
    title: str | None = Field(default=None, min_length=1, max_length=100) 
    content: str | None = Field(default=None, min_length=1) 

