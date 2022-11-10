from http.client import HTTPException
from uuid import UUID, uuid4
from fastapi import FastAPI
from models import User, Role, Gender, UserUpdateRequest
from typing import List
app = FastAPI()

db: List[User] = [
    User(
        id=uuid4(), 
        first_name= "Ambrose", 
        last_name= "Otundo",
        middle_name = "Heyman",
        gender = Gender.female,
        roles= [Role.student]
    ),

    User(
        id=uuid4(), 
        first_name= "Ambrse", 
        last_name= "Ot",
        middle_name = "yman",
        gender = Gender.male,
        roles= [Role.admin, Role.user]
    )
    
]

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/api/v1/users")
async def fetch_users():
    return db

@app.post("/api/v1/users")
async def reg_user(user: User):
    db.append(user)
    return {"id": user.id}

@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db:
        if user.id == user_id:
            db.remove(user)
            return 
    raise HTTPException(
        status_code = 404,
        detail= f"user with id: {user_id} does not exist"
    )

@app.put("/apiv1/users/{user_id}") 
async def update_user(user_update: UserUpdateRequest, user_id: UUID):
    for user in db: 
        if user.id == user_id: 
            if user_update.first_name is not None: 
                user.first_name = user_update.first_name 
            if user_update.last_name is not None: 
                user.last_name = user_update.last_name
            if user_update.middle_name is not None: 
                user.middle_name = user_update.middle_name 
            if user_update.roles is not None: 
                user.roles = user_update.roles
                return
    raise HTTPException( 
        status_code=404, 
        detail=f"user with id: {user_id} does not exists")