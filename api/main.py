from fastapi import FastAPI
from .database import engine
from .post.router import router as post_router
from .database import Base


app = FastAPI()
app.include_router(post_router)
Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "Hello World"}