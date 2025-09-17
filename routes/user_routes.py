from fastapi import APIRouter

from schemas.user_schemas import Register,Login,OTP,ResetData,User,Post,GetById,GetByTitle,UserId,FF,Follower,Following,Block
from controller.user import user_register,user_login,otp_sent,reset_password,user_add,user_post,getbyid,getbyititle,allpost,ff_post,find_follower,find_following,block_ff,unfollow,unblock




router = APIRouter()



# User register
@router.post("/register")
def register_user(data:Register):
    return user_register(data)


#User login
@router.get("/login")
def login_user(data:Login):
    return user_login(data)


#Otp sent
@router.get("/otp")
def sent_otp(data:OTP):
    return otp_sent(data)


#Reset password
@router.patch("/reset")
def password_reset(data:ResetData):
    return reset_password(data)


#Add User
@router.post("/add")
def add_user(data:User):
    return user_add(data)

#POst on instagram
@router.post("/post")
def post_user(data:Post):
    return user_post(data)


#Get Post by id
@router.get("/getpost")
def postget(data:GetById):
    return getbyid(data)


#Get Post by title
@router.get("/getpostbytitle")
def getpost(data:GetByTitle):
    return getbyititle(data)



#get all Post
@router.get("/allpost")
def postall(data:UserId):
    return allpost(data)








#Msg show for follow and following
@router.post("/postff")
def xyz_ff(data:FF):
     return ff_post(data)


#unfollow
@router.post("/unfollow")
def unfollow_user(data:FF):
    return unfollow(data)


#block ff
@router.post("/block")
def ff_block(data:Block):
    return block_ff(data)

#unblock
@router.post("/unblock")
def unblock_user(data:Block):
    return unblock(data)



#Check follower by username
@router.get("/follower")
def xyz(data:Follower):
    return find_follower(data)


#Check following by username
@router.get("/following")
def following_find(data:Following):
    return find_following(data)



