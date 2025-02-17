# import dependeny
from fastapi import FastAPI
from . routers import posts,employeecrud
 
app= FastAPI()

app.include_router(posts.router)
app.include_router(employeecrud.router)
