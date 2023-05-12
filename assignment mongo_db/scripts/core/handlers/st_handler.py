from scripts.utils import db
from scripts.schemas import models
class Student_Routes:
    def get_all(self):
        data=db.all()
        return{"data":data}

    def create(self,data:models.Student):
        id=db.create(data)
        return {"inserted":True,"inserted_id":id}

    def get_one(self,name:str):
        data=db.get_one(name)
        return {"data":data}

    def delete(self,name:str):
        data=db.delete(name)
        return {"deleted":True,"deleted_count":data}

    def update(self,data:models.Student,name:str):
        print(name)
        data=db.update(data,name=name)
        return {"updated":True,"updated_count":data}
student_routes_obj=Student_Routes()