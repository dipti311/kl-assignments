'''from pydantic model import BaseModel
class tset(basemodel)
name:str
age:int
information:list(str)
email:str=None'''
#regix
from fastapi import FastAPI
app=FastAPI()
students={
    1: {
    "name":"dipti",
    "age":23

}}

@app.get("/")
async def root():
    return {"message":"hello dipti"}
@app.get("/get-students/{student_id}")
def student_id(student_id:int):
    return students[student_id]