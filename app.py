from flask import Flask, jsonify

app = Flask(__name__)

stores = [
    {
        'name': "restuarant A",
        'items': [
            {
                'name': 'item1',
                'price': 9.22
            }
        ]
    }
]


# POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    pass

# GET /store/<string:name>
@app.route('/store/<string:name>', methods=['POST']) # represent to homepage
def get_store(name):
    pass

# GET /store
@app.route('/store/')
def get_stores():
    return jsonify({'stores':stores})

# POST /store/<string:name>/item {name:, price:"}
@app.route('/<string:name>/item', methods=['POST'])
def create_store_in_store(name):
    pass

# POST /store/<string:name>/item
@app.route('/<string:name>/item', methods=['POST'])
def get_item_in_store(name):
    pass

app.run(port=5500)