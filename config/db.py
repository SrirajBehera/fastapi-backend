import os
import motor.motor_asyncio
from dotenv import load_dotenv

load_dotenv()

mongodb_uri = os.getenv("MONGODB_URI")

client = motor.motor_asyncio.AsyncIOMotorClient(mongodb_uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    db = client.cosmocloud
    student_collection = db.get_collection("student")
except Exception as e:
    print(e)
