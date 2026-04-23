from pymongo import MongoClient

# 🔥 Connect MongoDB
client = MongoClient("mongodb://localhost:27017/")

# 🔥 Database
db = client["ai_gym"]

# 🔥 Collections
habit_collection = db["habits"]