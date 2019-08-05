from flask import jsonify, request, url_for, g, abort
from app import db
from app.models import User
from app.models import Sport, Athlete
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request


@bp.route('/users/<int:id>', methods=['GET'])
@token_auth.login_required
def get_user(id):
    return jsonify(User.query.get_or_404(id).to_dict())


@bp.route('/users', methods=['GET'])
@token_auth.login_required
def get_users():
    data = [user.to_dict() for user in User.query.all()]
    return jsonify(data)


@bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json() or {}
    if 'username' not in data or 'email' not in data or 'password' not in data:
        return bad_request('must include username, email and password fields')
    if User.query.filter_by(username=data['username']).first():
        return bad_request('please use a different username')
    if User.query.filter_by(email=data['email']).first():
        return bad_request('please use a different email address')
    user = User()
    user.from_dict(data, new_user=True)
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    response.status_code = 201
    response.headers['Location'] = url_for('api.get_user', id=user.id)
    return response


@bp.route('/users/<int:id>', methods=['PUT'])
@token_auth.login_required
def update_user(id):
    if g.current_user.id != id:
        abort(403)
    user = User.query.get_or_404(id)
    data = request.get_json() or {}
    if 'username' in data and data['username'] != user.username and \
            User.query.filter_by(username=data['username']).first():
        return bad_request('please use a different username')
    if 'email' in data and data['email'] != user.email and \
            User.query.filter_by(email=data['email']).first():
        return bad_request('please use a different email address')
    user.from_dict(data, new_user=False)
    db.session.commit()
    return jsonify(user.to_dict())

@bp.route('/ping')
@token_auth.login_required
def ping():
    return 'pong'


# TODO: Add own CRUD routes to work with your models

#create/POST Sports
@bp.route('/sports', methods=['POST'])
@token_auth.login_required
def create_sport():
    sport_data = request.get_json() or {}
    
    # Would I include the three if statements for Sport such as the ones in create_user() and update_user()?
    sport = Sport(name = sport_data.get("name"), objective = sport_data.get("objective"))
    db.session.add(sport)
    db.session.commit()
    return jsonify(sport.to_dict())

#read/GET Sport
@bp.route('/sports/<int:id>', methods=['GET'])
@token_auth.login_required
def read_one_sport():
    sport_get_id = Sport.query.get(id)
    return jsonify(sport_get_id.to_dict())

@bp.route('/sports', methods=['GET'])
@token_auth.login_required
def read_all_sport():
    sports = Sport.query.all()
    sports = [sport.to_dict() for sport in sports]
    return jsonify(sports)

#update/PUT Sport
def update_one_sport():
    pass

def update_all_sport():
    pass

#delete/DELETE Sport
def delete_one_sport():
    pass

#create/POST Athlete
def create_one_athlete():
    pass

#read/GET Athlete
def get_one_athlete():
    pass

def get_all_athlete():
    pass

#update/PUT Athlete
def update_one_athlete():
    pass

#delete/DELETE Athlete
def delete_one_athlete():
    pass