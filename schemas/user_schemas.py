from pydantic import BaseModel



class Register(BaseModel):
    username:str
    email:str
    password:str    



class Login(BaseModel):
    username:str
    password:str

class OTP(BaseModel):
    email:str  


class ResetData(BaseModel):
    username:str
    otp:str
    new_password: str   


class User(BaseModel):
    id:str
    name:str
    username:str
    email:str





class Post(BaseModel):

    username:str
    post_id:str
    contant:str
    title:str
    
class GetById(BaseModel):
    post_id:str

class GetByTitle(BaseModel):
    title:str   


class UserId(BaseModel):
    username:str




class FF(BaseModel):
    follow_by:str
    follow_to:str

class Follower(BaseModel):
    username:str

class Following(BaseModel):
    username:str