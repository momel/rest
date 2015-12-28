from flask import (
    Flask,
    jsonify,
    request,
    abort,
    make_response,
    url_for
)

app = Flask(__name__)

users = [

     {
        'id': 1,
        'name': u'Criss Baker',
        'login': u'admin',
        'password': 'admin',
        'email': 'admin@host.com',
        'role': 'ADMIN'
    },

    {
        'id': 2,
        'name': u'Samuel Hitrou',
        'login': u'manager',
        'password': 'manager',
        'email': 'manager@host.com',
        'role': 'MANAGER'
    },

    {
        'id': 3,
        'name': u'Stasy Hisard',
        'login': u'user',
        'password': 'user',
        'email': 'sthis@host.com',
        'role': 'USER'
    },

    {
        'id': 4,
        'name': u'Mark Mayo',
        'login': u'muser',
        'password': 'muser',
        'email': 'mamao@host.com',
        'role': 'USER'
    },

]

app.config.update(dict(
    DEBUG = True
))

@app.route('/users/all', methods=['GET'])
def getAllUsers():
    return jsonify({'users': users})

@app.route("/users/auth/login/<int:user_id>", methods=['GET'])
def getCurrentUser(user_id):
    user = filter(lambda u: u['id'] == user_id, users)
    if len(user) == 0:
        abort(404)
    return jsonify({'user': user[0]})

@app.route("users/auth/login", methods=["POST"])
def login_user():
    if not request.json or not 'name' in request.json:
        abort(400)
    user = {
        'id': users[-1]['id'] + 1,
        'name': request.json['name'],

    }
    users.append(user)
    return jsonify({'user', user}), 201


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': error}), 404)

if __name__ == '__main__':
    app.run()
