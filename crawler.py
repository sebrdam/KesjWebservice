from app import app, jsonify, request, auth


_definitions = [
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


@app.route('/crawler/get', methods=['GET'])
@auth.login_required
def get_webdefinitions():
    return jsonify({'definitions': _definitions})


@app.route('/crawler/post', methods=['POST'])
@auth.login_required
def post_data():
    return "Post data"
