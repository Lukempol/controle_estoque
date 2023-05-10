import pymongo

def mongo_conect():
    client = pymongo.MongoClient(str(os.getenv('MONGODB_URL')))
    db = client.todo_sample
    collection = db.todos
    return collection