from flask import Flask, jsonify, request, make_response
from flask.ext.httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    'kesj': 'kesj',
    'edwin': 'edwin',
    'sebastiaan': 'sebastiaan'
}


@app.route('/')
@auth.login_required
def index():
    return "Hello, %s!" % auth.username()


@auth.get_password
def get_pw(username):
    if username in users:
        return users.get(username)
    return None


@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)


""" CRAWLER """
definitions = [
    {
        "provider": "Alternate",
        "category": "Moederbord",
        "subcategory": "AMD",
        "url": "http://127.0.0.1/alternate/index1.htm",
        "pattern": "<div class=\"listRow\">(.*?)<div class=\"clear\">",
        "subpatternprijs": "&euro; (.*?)</sup>",
        "subpatternlink": "<a class=\"productLink\" href=\"(.*?)\"",
        "subpatternomschrijving": "<span class=\"pic\" title=\"(.*?)\""
    },
    {
        "provider": "Alternate",
        "category": "ddr3",
        "subcategory": "none",
        "url": "http://127.0.0.1/alternate/index1.htm",
        "pattern": "<div class=\"listRow\">(.*?)<div class=\"clear\">",
        "subpatternprijs": "&euro; (.*?)</sup>",
        "subpatternlink": "<a class=\"productLink\" href=\"(.*?)\"",
        "subpatternomschrijving": "<span class=\"pic\" title=\"(.*?)\""
    }
]


@app.route('/crawler/get', methods=['GET'])
def get_webdefinitions():
    definitions = [
        {
            "provider": "Alternate",
            "category": "Moederbord",
            "subcategory": "AMD",
            "url": "http://127.0.0.1/alternate/index1.htm",
            "pattern": "<div class=\"listRow\">(.*?)<div class=\"clear\">",
            "subpatternprijs": "&euro; (.*?)</sup>",
            "subpatternlink": "<a class=\"productLink\" href=\"(.*?)\"",
            "subpatternomschrijving": "<span class=\"pic\" title=\"(.*?)\""
        },
        {
            "provider": "Alternate",
            "category": "ddr3",
            "subcategory": "none",
            "url": "http://127.0.0.1/alternate/index1.htm",
            "pattern": "<div class=\"listRow\">(.*?)<div class=\"clear\">",
            "subpatternprijs": "&euro; (.*?)</sup>",
            "subpatternlink": "<a class=\"productLink\" href=\"(.*?)\"",
            "subpatternomschrijving": "<span class=\"pic\" title=\"(.*?)\""
        }
    ]
    return jsonify(definitions)


@app.route('/crawler/post', methods=['POST'])
def post_data():
    return "Post data"


""" PRODUCTS """
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


if __name__ == '__main__':
    app.run(debug=True)
