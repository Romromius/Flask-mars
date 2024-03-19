import sqlalchemy.exc
from flask import *
from flask_restful import *

import api_argparser
from data import db_session
from data.users import User


def abort_if_users_not_found(user_id):
    session = db_session.create_session()
    users = session.query(User).get(user_id)
    if not users:
        abort(404, message=f"user {user_id} not found")


class UsersResource(Resource):
    def get(self, user_id):
        abort_if_users_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).filter(User.id == user_id)[0]
        return jsonify({'user': user.to_dict(only=('id', 'name', 'email'))})

    def delete(self, user_id):
        abort_if_users_not_found(user_id)
        session = db_session.create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UserListResource(Resource):
    def get(self):
        session = db_session.create_session()
        users = session.query(User).all()
        return jsonify({'users': [item.to_dict(
            only=('id', 'name', 'email')) for item in users]})

    def post(self):
        args = api_argparser.user_parse()
        session = db_session.create_session()
        user = User()
        user.name = args['name']
        user.email = args['email']

        user.set_password(args['password'])
        session.add(user)
        try:
            session.commit()
        except sqlalchemy.exc.IntegrityError:
            return jsonify({'message': 'this email is unavailable'})
        return jsonify({'id': user.id})
