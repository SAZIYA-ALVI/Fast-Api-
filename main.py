from fastapi import FastAPI # fastapi framework

app = FastAPI()

@app.get("/")
def hello():
    return{"message": "my first API is working"}

@app.get("/about")
def about():
    return{"project": "This is my first API project using"}

