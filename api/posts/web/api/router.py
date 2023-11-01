from typing import Annotated
from fastapi import APIRouter, Depends, Response, status

from .schemas import *
from ...repository.repository import SQLPostRepository

router = APIRouter(prefix="/post", tags=["post"])

Repository = Annotated[SQLPostRepository, Depends(SQLPostRepository)]


@router.get("/", response_model=list[PostResponseSchema])
def get_posts(repo: Repository) -> list[PostResponseSchema]:
    return repo.list()


@router.post("/", response_model=PostResponseSchema, status_code=status.HTTP_201_CREATED)
def create_post(post: BasePostSchema, repo: Repository) -> PostResponseSchema:
    post = repo.add(post)
    return post

@router.get("/{post_id}", response_model=PostResponseSchema)
def get_post(post_id: int, repo: Repository) -> PostResponseSchema:
    return repo.get(post_id)


@router.put("/{post_id}", response_model=PostResponseSchema)
def update_post(post_id: int, updated_post: PostUpdateSchema, repo: Repository) -> PostResponseSchema:
    return repo.update(post_id, updated_post)



@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, repo: Repository):
    repo.delete(post_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
    

