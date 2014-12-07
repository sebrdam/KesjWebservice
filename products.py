from app import app, jsonify, request, auth


_products = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/products/get', methods=['GET'])
@auth.login_required
def getProducts():
    if request.args.get('id', '') != '':
        return __getSingle(request.args.get('id', ''))

    elif request.args.get('category', '') != '':
        return __getMultiple(request.args.get('category', ''))

    else:
        return 'Missing params.'


def __getSingle(id):
    return jsonify({'products': _products[0]})


def __getMultiple(category):
    return jsonify({'products': _products})
