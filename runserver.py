from flask import (
    Flask,
    json,
    jsonify,
    request,
    abort,
    make_response,
    url_for,
    Response,
    session,
    escape
)

app = Flask(__name__)

users = [{'id': 1,
          'name': u'Criss Baker',
          'login': u'admin',
          'password': 'admin',
          'email': 'admin@host.com',
          'role': 'ADMIN'},
         {'id': 2,
          'name': u'Samuel Hitrou',
          'login': u'manager',
          'password': 'manager',
          'email': 'manager@host.com',
          'role': 'MANAGER'},
         {'id': 3,
          'name': u'Stasy Hisard',
          'login': u'user',
          'password': 'user',
          'email': 'sthis@host.com',
          'role': 'USER'},
         {'id': 4,
          'name': u'Mark Mayo',
          'login': u'muser',
          'password': 'muser',
          'email': 'mamao@host.com',
          'role': 'USER'}]

app.config.update(dict(DEBUG=True))
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

@app.route('/users/all', methods=['GET'])
def getAllUsers():
    print session
    return Response(json.dumps(users), mimetype='application/json')
    # return jsonify({'users': users})


@app.route("/users/current", methods=['GET'])
def getCurrentUser():
    print "POINT GET 1"
    print session
    if 'login' in session:
        print "POINT GET 2"
        print ('Logged in as ', escape(session['login']))
        user = {}
        user = filter(lambda u: u['login'] == session['login'], users)
    # if len(user) == 0:
      #  abort(404)
    # return jsonify({'user': user[0]})
    return Response(json.dumps(user), mimetype='application/json')


@app.route("/users/auth/login", methods=["POST"])
def login_user():
    if not request.json or not 'login' in request.json:
        abort(400)
    print "POINT : 1"
    user = filter(lambda u: u['login'] == request.json.get('login'), users)
    if len(user) == 0:
        abort(404)
    else:
        session['login'] = request.json.get("login")
    print "Session: ", session['login']
    return "message"


@app.route("/users/auth/signup", methods=["POST"])
def signup_user():
    if not request.json or not 'login' in request.json:
        abort(400)
    user = {'id': users[-1]['id'] + 1,
            'login': request.json['login'],}
    session['logged_in'] = True
    print session
    users.append(user)
    # return jsonify({'user', user}), 201
    return Response(json.dumps(user), mimetype='application/json')


@app.route("/users/auth/logout", methods=["POST"])
def logout_user():
    if not request.json or not 'id' in request.json:
        abort(400)
    return jsonify({"message": "Have a nice day!"})
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': error}), 404)

if __name__ == '__main__':
    app.run()
