from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/about")
def read_about():
    return {"message": "About Page"}

class User(BaseModel):
    name: str
    age: int
    email: str


@app.post("/users")
def create_user(user: User):
    return user