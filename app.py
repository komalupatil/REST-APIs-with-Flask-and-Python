from flask import Flask, jsonify, request, render_template

app = Flask(__name__)


stores = [
    {
        'name': 'Wonderful',
        'items': [
            {
            'name': 'My item',
            'price': 30
            }
        ]   
    }
]

@app.route('/')  #'http://www.google.com/'
def home():
    return render_template('index.html')

#wrt server not browser
#post --> used to receive data
#get ---> used to send data back only

#POST /store data: {name:}
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()   # get the data sent by browser to us
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)


#GET /store/<string:name>
@app.route('/store/<string:name>', methods=['GET'])
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'Store not found'})


#GET /store
@app.route('/store/', methods=['GET'])
def get_all_store():
    return jsonify({'stores': stores})


#POST /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(store)
    return jsonify({'message': 'Store not found'})


#GET /store/<string:name>/item
@app.route('/store/<string:name>/item', methods=['GET'])
def get_item_in_sotre(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'Store not found'})


app.run(port=5000)