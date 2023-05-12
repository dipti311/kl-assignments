import pymongo  
mongoURI =  "mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23"
client=pymongo.MongoClient(mongoURI)
db=client.interns_b2_23
collection = db["dipti_db"]
def create(data):
    data=dict(data)
    response=collection.insert_one(data)
    return str(response.inserted_id)
def all():
    response = collection.find({})
    data=[]
    for i in response:
        i["_id"]=str(i["_id"])
        data.append(i)
    return data
def get_one(condition):
    response=collection.find_one({"name":condition})
    response["_id"]=str(response["_id"])
    return response
def update(data,name):
    data=dict(data)
    response = collection.update_one({"name": name}, {"$set": data},upsert=True)

    return response.modified_count
def delete(name):
    response=collection.delete_one({"name":name})
    return response.deleted_count