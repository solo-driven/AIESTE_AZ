from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from ..repository.exceptions import PostNotFoundError
from .api.router import router as post_router



app = FastAPI()
app.include_router(post_router)

@app.exception_handler(PostNotFoundError)
def post_not_found_exception_handler(request: Request, exc: PostNotFoundError):
    return JSONResponse(
        status_code=404,
        content={"message": str(exc)},
    )

@app.get("/")
def root():
    return {"message": "Hello World"}