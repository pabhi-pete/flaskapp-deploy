from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        "name": "sas",
        "items": [
            {
                "name": "item1",
                "price": 9.22
            }
        ]
    }
]


# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>', methods=['POST']) # represent to homepage
def get_store(name):
    # iterate over stores
    # if the store name matches, return it
    # if non-match, return an error message
    # try:
    #     for n in stores['name']:
    #         if n == name:
    #             return jsonify(n)
    # except ValueError:
    #     return jsonify({'Sorry! cannot find store: {name} in our lists'})
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
        return jsonify({'message': 'store not found'})
        

# GET /store
@app.route('/store/')
def get_stores():
    return jsonify({'stores':stores})

# POST /store/<string:name>/item {name:, price:"}
@app.route('/<string:name>/item', methods=['POST'])
def create_store_in_store(name):
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request.data['name'],
                'price': request.data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})
    
# POST /store/<string:name>/item
@app.route('/<string:name>/item', methods=['POST'])
def get_item_in_store(name):
    for store in stores['name']:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})


app.run(port=5500)