from flask import Flask, render_template, request
from db import get_all,add_food,get_food_by_name,update
app = Flask(__name__)

@app.route('/food-edit/<name>')
def edit_food(name):
    food = get_food_by_name(name)
    print(food)
    return render_template('food-edit.html', food = food)

@app.route('/food-edit/<name>', methods = ['POST'])
def post_edit_food(name):
    # food = get_food_by_name(name)
    food_name = request.form.get('name')
    food_price = request.form.get('price')

    update(food_name,food_price)
    
    return  render_template('food.html',data=get_all())

# foods = [
#     {
#         'name':'cơm rang',
#         'price':30,
#         'image_url':'https://media.cooky.vn/recipe/g1/483/s800x500/recipe483-635678063026944007.jpg'
#     },
#     {
#         'name':'cơm gà',
#         'price':100,
#         'image_url':'https://media.foody.vn/res/g70/692641/prof/s/foody-mobile-foody-mobile-foody-a-922-636428010244489101.jpg'
#     }
# ]


@app.route('/')
def get_food():
    return render_template('food.html',data=get_all())


@app.route('/',methods=["POST"])
def post_food():
    food_name = request.form.get('name')
    food_price = request.form.get('price')
    food_image = request.form.get('image_url')

    # foods.append({
    #     'name':food_name,
    #     'price':food_price,
    #     'image_url':food_image
    # })

    add_food(food_name,food_price)
    return render_template('food.html',data=get_all())


if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
        