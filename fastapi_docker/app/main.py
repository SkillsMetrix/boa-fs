
from fastapi import FastAPI

app= FastAPI()

users=[{'id':101,'uname':'Admin','email':'admin@mail.com'}]

@app.get('/')
def loadData():
    return {'message':'welcome to FastAPI'}

@app.get('/loadusers')
def loadUsers():
    return {'message':users}