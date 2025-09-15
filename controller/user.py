from fastapi import HTTPException
import random

#Register User
s=["@","#","$","&"]
data_db=[]
def user_register(data):
   for i in data_db:
      if data.username==i["username"]:
         raise HTTPException(status_code=409,detail="username already exists")
      if data.email==i["email"]:
          raise HTTPException(status_code=409,detail="email already exists")
      
   if len(data.password)>=8:
      for x in s:
       if x in data.password:
        data_db.append(data.dict())
        print(data_db)
        return {"Sucess":True,"Status Code":"200","msg":"suceesfully register"}
      raise HTTPException(status_code=409,detail="not special charctr")
   raise HTTPException (status_code=409,detail="length of your password less than 8")   





#Login User

def user_login(data):
   for i in data_db:
      if data.username==i["username"] and data.password==i["password"]:
            return {"Sucess":True,"Status Code":"200","msg":"successfully Login"}
   raise HTTPException(status_code=409,detail="wrong your information")





#Opt sent
new_otp=[]
def otp_sent(data):
   for i in data_db:
      if data.email==i["email"]:
         otp=random.randint(1111,9999)
         new_otp.append(str(otp))
         print(new_otp)
         return {"sucess":True,"status":201,"msg":f"sent otp this email {data.email}","OTP":otp}
   raise HTTPException(status_code=409,detail="This email is not register")




#Reset password

a=["@","#","$","&"]
def reset_password(data):
   for i in data_db:
      if data.username==i["username"]:
         if data.otp in new_otp:
            if len(data.new_password)>=8:
               for r in a:
                  if r in data.new_password:
                   i["password"]=data.new_password
                   return {"sucess":True,"status":201,"msg":"reset your password"}
               raise HTTPException (status_code=409,detail="You Give Special Chracter in password")
            raise HTTPException(status_code=409,detail="Your password length less than 8")
         raise HTTPException(status_code=409,detail="your otp not match ")
   raise HTTPException(status_code=409,detail="your username not register")



# Add user 
user_db=[]
def user_add(data):

   for i in user_db:
      if data.id==i["id"]:
         raise HTTPException(status_code=409,detail="your id is already exists")
      if data.username==i["username"]:
         raise HTTPException(status_code=409,detail="username is already exists")
      if data.email==i["email"]:
         raise HTTPException(status_code=409,detail="your email is already exists")
   if data.name:
      user_db.append(data.dict())
      print(user_db)
      return {"msg":"add user"}
   raise HTTPException(status_code=409,detail="please entre your name")

   
#User post 
post_data=[]
def user_post(data):
   for i in user_db:
      if data.username==i["username"]:
         for x in post_data:
             if data.post_id==x["post_id"]:
              raise HTTPException (status_code=409,detail="post is already exists") 
         if True:    
           post_data.append(data.dict())
           print(post_data)
           return {"msg":"post done"}
   raise HTTPException (status_code=409,detail="Not match your username")  



#Post get by id 
def getbyid(data):
   for i in post_data:
      if data.post_id==i["post_id"]:
         return {"msg":"Done","your Post":i}
   raise HTTPException (status_code=409,detail="Not ,match your id ") 



#Get by title
title=[]
def getbyititle(data):
   for i in post_data:
      if data.title==i["title"]:
       title.append(i)
   if len(title)>0:
      return {"sucess":True,"status":201,"msg":"yours title ","title":title}
   raise HTTPException(status_code=409,detail="Not match your title")


#Get all post by username

all_post=[]
def allpost(data):
   for i in post_data:
      if data.username==i["username"]:
         all_post.append(i)
   if len(all_post)>0:
        return {"Sucess":True,"Status Code":"200","All Post":all_post}
   raise HTTPException(status_code=409,detail="not match username")




#Instagram User Dummy Data
instagram_users=[{"username":"vikram0001","email":"vikram005104@gmail.com","password":"vikram123"},
                 {"username":"prince0001","email":"pv005104@gmail.com","password":"prince123"},
                {"username":"jatin0001","email":"jatin005104@gmail.com","password":"jatin123"}]

new_data=[]
def ff_post(data):
   for i in instagram_users:
      if i["username"]==data.follow_by :
       for x in instagram_users:
           if x["username"]==data.follow_to :
              new_data.append(data.dict())
              print(new_data)
              return {"Sucess":True,"Status Code":"200","msg":f"{data.follow_by}  Follow to {data.follow_to}"}
       raise HTTPException(status_code=409,detail=f"You can not follow to {data.follow_to} Because do not exists in data base") 
   raise HTTPException(status_code=409,detail=f" {data.follow_by} You are not exists in data base") 




# Check User Follower
my_follower=[]
def find_follower(data):
   for i in new_data:
      if data.username==i["follow_to"]:
         my_follower.append(i["follow_by"])
         print(my_follower)
   if len(my_follower)>=0:
      return {"Sucess":True,"Status Code":"200","Msg":f"Your Follower {my_follower}"}   
   raise {"Msg":"Not follower you"}   

# Check User Following
my_following=[]
def find_following(data):
   for  i in new_data:
      if data.username==i["follow_by"]:
         my_following.append(i["follow_to"])
         print(my_following)
   if len(my_following)>=0:
      return   {"Sucess":True,"Status Code":"200","Msg":f"Your following {my_following}"} 
   raise {"Msg":"your not follow to others"}  
        


