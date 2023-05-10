import pymongo

def mongo_conect():
    client = pymongo.MongoClient("mongodb+srv://Lukempol:0QW9Lsq0Sl14JZhe@cluster0.qgqcm.mongodb.net/?retryWrites=true&w=majority")
    db = client.todo_sample
    collection = db.todos
    return collection