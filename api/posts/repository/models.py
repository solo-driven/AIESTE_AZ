from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func  # Import func to use UTC timestamps
from sqlalchemy.orm import declarative_base
from . import engine

from .utils import IPost



Base = declarative_base()

class FinalMeta(type(Base), type(IPost)):
    pass


class Post(IPost, Base, metaclass=FinalMeta):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=False, onupdate=func.now(), default=func.now())


    def update(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def dict(self):
        print(self.__dict__)
        return self.__dict__
   
Base.metadata.create_all(bind=engine)
