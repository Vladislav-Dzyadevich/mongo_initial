from pymongo import MongoClient
from bson.objectid import ObjectId

# Підключення до MongoDB
client = MongoClient('localhost', 27017)
db = client['cats']  
collection = db['cat_profiles']  

# Create
def create_cat_profile(name, age, features):
    cat_profile = {
        "name": name,
        "age": age,
        "features": features
    }
    result = collection.insert_one(cat_profile)
    print("Cat profile created with id:", result.inserted_id)


# Read
def read_all_cat_profiles():
    cursor = collection.find({})
    for cat_profile in cursor:
        print(cat_profile)


def read_cat_profile_by_name(name):
    cat_profile = collection.find_one({"name": name})
    if cat_profile:
        print(cat_profile)
    else:
        print("Cat profile with name '{}' not found.".format(name))


# Update
def update_cat_age(name, new_age):
    result = collection.update_one({"name": name}, {"$set": {"age": new_age}})
    if result.modified_count > 0:
        print("Cat age updated successfully.")
    else:
        print("Cat profile with name '{}' not found.".format(name))


def add_feature_to_cat(name, new_feature):
    result = collection.update_one({"name": name}, {"$push": {"features": new_feature}})
    if result.modified_count > 0:
        print("New feature added to cat profile successfully.")
    else:
        print("Cat profile with name '{}' not found.".format(name))


# Delete
def delete_cat_profile_by_name(name):
    result = collection.delete_one({"name": name})
    if result.deleted_count > 0:
        print("Cat profile deleted successfully.")
    else:
        print("Cat profile with name '{}' not found.".format(name))


def delete_all_cat_profiles():
    result = collection.delete_many({})
    print("All cat profiles deleted. Total deleted count:", result.deleted_count)


# Приклад використання функцій
if __name__ == "__main__":
    create_cat_profile("barsik", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    create_cat_profile("Микола", 32, ["ходить", "кусається", "зелений"])
    create_cat_profile("Володимир", 3, ["ходить в капці", "дає себе гладити", "рудий"])
    create_cat_profile("Дмитро", 3, ["ходить в капці", "дає себе гладити", "рудий"])


    print("\nAll cat profiles:")
    read_all_cat_profiles()
    print("\nCat profile by name:")
    read_cat_profile_by_name("barsik")
    print("\nUpdate cat age:")
    update_cat_age("barsik", 5)
    print("\nAdd feature to cat:")
    add_feature_to_cat("barsik", "лінивий")
    print("\nCat profile by name after update:")
    read_cat_profile_by_name("barsik")
    print("\nDelete cat profile by name:")
    delete_cat_profile_by_name("barsik")
    print("\nAll cat profiles after deletion:")
    read_all_cat_profiles()
