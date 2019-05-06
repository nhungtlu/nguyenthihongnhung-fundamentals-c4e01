import pymongo

client = pymongo.MongoClient("mongodb+srv://nhung:VK17gJAQLcGhyzQn@cluster0-pj6rg.mongodb.net/test?retryWrites=true")
db = client.test

def update(name,price):
    db.foods.update_one({'name': name},{'$set' : {'price':price}})

def get_food_by_name(name):
    return db.foods.find_one({'name':name})


# db.foods.insert_one({'name': "cơm rang",'price':'15'})
# db.foods.insert_one({'name': "cơm gà",'price':'20'})

# # liệt kê tất cả các user đang có
# print(list(db.foods.find({})))

# # Tìm kiếm các user có tên là cơm rang
# print(list(db.foods.find({'name': 'cơm rang'})))

# # tìm kiếm 1 user có tên là cơm rang 
# print(db.foods.find_one({'name':'cơm rang'}))

# db.foods.update_one({'name':'cơm rang'},{'$set':{'price': 30 }})

# db.foods.delete_one({'name':'cơm rang'})


def get_all():
    # lấy tất cả các foods
    return list(db.foods.find({}))


def add_food(name,price):
    db.foods.insert_one({'name': name, 'price': price})