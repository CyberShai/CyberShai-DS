from fastapi import Depends, FastAPI


app = FastAPI(title="CyberShai API",
    description="REST API which returns statistics for CyberShai project.",
    version="0.1",)


# @app.get("/", tags=["API Root"])
# def root():
#     return {"message": "Hello World"}
@app.get("/", tags=["API Root"])
def welcome():
    return {"message": "Welcome to CyberShai API"}