from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Modelo de dados
class User(BaseModel):
    id: int
    name: str
    email: str

# Banco de dados simulado
users = []

@app.get("/api/users")
def get_users():
    return users

@app.post("/api/users")
def create_user(user: User):
    users.append(user)
    return user

@app.get("/api/users/{user_id}")
def get_user(user_id: int):
    return next((user for user in users if user.id == user_id), None)

@app.put("/api/users/{user_id}")
def update_user(user_id: int, user: User):
    for idx, existing_user in enumerate(users):
        if existing_user.id == user_id:
            users[idx] = user
            return user
    return None

@app.delete("/api/users/{user_id}")
def delete_user(user_id: int):
    global users
    users = [user for user in users if user.id != user_id]
    return {"message": "User deleted"}
