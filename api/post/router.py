from fastapi import APIRouter, Depends, HTTPException, Response, status
from .models import Post
from .schemas import PostSchema, PostUpdateSchema
from ..database import  get_db
from sqlalchemy.orm.session import Session

router = APIRouter(prefix="/post", tags=["post"])

@router.get("/")
def get_posts(db: Session = Depends(get_db)) -> list[PostSchema]:
    return db.query(Post).all()


@router.post("/")
def create_post(post: PostSchema, db: Session = Depends(get_db)) -> PostSchema:
    post = Post(**post.model_dump())
    db.add(post)
    db.commit()
    db.refresh(post)
    return post

@router.get("/{post_id}")
def get_post(post_id: int, db: Session = Depends(get_db)) -> PostSchema:
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    return post

@router.put("/{post_id}", response_model=PostSchema)
def update_post(post_id: int, updated_post: PostUpdateSchema, db: Session = Depends(get_db)) -> PostSchema:

    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
        raise HTTPException(status_code=404, detail="Post not found")

    post.update(**updated_post.model_dump(exclude_unset=True))  # Update object attributes
    db.commit()
    db.refresh(post)  # Refresh the object to get the updated values
    return post



@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(Post).filter(Post.id == post_id).first()

    if not post:
         raise HTTPException(status_code=404, detail="Post not found")
    
    db.delete(post)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)
    

