
from fastapi import FastAPI,HTTPException,status,APIRouter
from fastapi.params import Body
from random import randrange
from .. import schema

router=APIRouter(tags=["BOA UserPost Application"])

my_post=[{"title":"welcome title","content":"dummy content","id":101}]

# search function

def findPost(id):
    for i,p in enumerate(my_post):
        if p['id'] == id:
            return i


# load the data using get

@router.get("/loadposts")
def loadallposts():
    return {"dummy-message": my_post}

# get specific record by passing ID
@router.get("/loadpost/{id}")
def loadById(id:int):
    post=findPost(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Given ID not found')
    else:
    
        return {"User Found":post}
    
# delete record by passing ID
@router.delete("/deletepost/{id}")
def deleteById(id:int):
    post=findPost(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Given ID not found')
    my_post.pop(post)
    return {"message": "user deleted"}

# update record by passing ID
@router.put("/updatepost/{id}")
def updateById(id:int,payload:schema.Post):
    post=findPost(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail='Given ID not found')
    postdata=payload.dict()
    postdata['id']=id
    my_post[post]=postdata
    return {"message": "user updated"}


# add the new post

@router.post("/addpost",status_code=status.HTTP_204_NO_CONTENT)
def addpost(payload: schema.Post):
    data= payload.dict()
    data['id']=randrange(0,1000)
    my_post.append(data)
    return {"message":data}

