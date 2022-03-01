from typing import List
from fastapi import status, HTTPException, Depends, APIRouter
from .. import models, schemas, utils
from sqlalchemy.orm import Session
from ..database import get_db

router = APIRouter(
    prefix="/users",
    tags=['Users']

)

@router.post("/", status_code = status.HTTP_201_CREATED)


def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):

    #hash password - user.password
    hash_pass= utils.hash(user.password)
    user.password = hash_pass

    new_user = models.User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.get("/{id}", response_model=schemas.UserResponse)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail = f"User with id: {id} does not exist")
    
    post = db.query(models.Post).filter(models.Post.id == id).first()

    return user

@router.get("/",response_model=List[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    #cursor.execute("""SELECT * FROM posts""")
    #posts=cursor.fetchall()
    users = db.query(models.User).all()
    return users