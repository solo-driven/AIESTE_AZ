from . import SessionLocal
from .exceptions import PostNotFoundError
from .models import Post
from .utils import IPostRepository, IPost
from sqlalchemy.orm.session import Session
from datetime import datetime




#Post "implements" IPost

class SQLPostRepository(IPostRepository):
    table = Post

    def __init__(self):
        self.session: Session = SessionLocal()

    def get(self, id: int) -> Post:
        post = self.session\
            .query(self.table)\
            .filter(self.table.id == id)\
            .first()
        
        if not post:
            raise PostNotFoundError(id)
        
        return  post

    def add(self, post: IPost) -> Post: 
        post = self.table(**post.dict())
        self.session.add(post)
        self.session.commit()
        self.session.refresh(post)
        return post

    def update(self, id: int, updated_post: IPost) -> Post:
        post = self.session.query(self.table).filter(self.table.id == id).first()

        if not post:
            raise PostNotFoundError(id)

        post.update(**updated_post.dict())  # Update object attributes
        
        self.session.commit()
        self.session.refresh(post)  # Refresh the object to get the updated values
        return post

    def list(self, limit: int = None, offset: int = None, created_between: tuple[datetime, datetime] | None = None) -> list[Post]:
            query = self.session.query(self.table)

            if limit is not None:
                query = query.limit(limit)

            if offset is not None:  
                query = query.offset(offset)

            if created_between is not None:
                start_date, end_date = created_between
                query = query.filter(self.table.created_at.between(start_date, end_date))

            return query.all()
    
    def delete(self, id: int) -> None:
        post = self.session.query(self.table).filter(self.table.id == id).first()

        if not post:
            raise PostNotFoundError(id)
        
        self.session.delete(post)
        self.session.commit()



