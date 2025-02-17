
from fastapi import FastAPI,HTTPException,status,APIRouter
from fastapi.params import Body
from random import randrange
from .. import employee

router=APIRouter(tags=["Employee CRUD Application"])

my_emp=[{"uname":"admin","email":"admin@mail.com","id":101}]

# search function

 

@router.get("/loademps")
def loadallemps():
    return {"dummy-message": my_emp}



@router.post("/addemp")
def addUser(payload: employee.Employee):
    data= payload.dict()
    data['id']=randrange(0,1000)
    my_emp.append(data)
    return {"message":data}

