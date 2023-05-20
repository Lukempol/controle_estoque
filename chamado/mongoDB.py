import pymongo
from dotenv import load_dotenv
import os

project_folder = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(project_folder)

def mongo_conect():
    client = pymongo.MongoClient(str(os.getenv('MONGODB_URL')))
    db = client.todo_sample
    collection = db.todos
    return collection