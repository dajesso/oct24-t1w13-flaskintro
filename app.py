from flask import Flask, request

app = Flask(__name__)

# felicis was here.
products = [
    {
        "id": 1,
        "title": 'Product 1',
        "price": 150
    },

    {
        "id": 2,
        "title": 'Felicis',
        "price": 60000
    }
]


@app.route('/')
def hello():
    return '<h2>Hello Felicis!</h2>'

@app.route('/second')
def another_router():
    return '<h2>Another route</h2>', 201

@app.route('/products')

def all_products():
    return products

 # get product with id == 1

@app.route('/products/<int:id>')

def one_product(id):
    print(id)
    filtered_products = list(filter(lambda p: p['id'] == id, products))
    print(list(filtered_products))
    return filtered_products[0]

@app.route('/can-vote')
def can_vote():

 
    print(request.args.get('age'))

    age = int(request.args.get('age'))
  
    if age >= 18:
        return {"message": "You can vote", "can_vote":True}
    else:
        return {"message": "You can't vote", "can_vote":False}

