from flask_restful import reqparse, abort, Api, Resource
from data import db_session
from data.users import User
from flask import Flask, render_template, redirect, session, make_response, request, abort, make_response, jsonify


def abort_if_news_not_found(news_id):
    session = db_session.create_session()
    news = session.query(Users).get(news_id)
    if not news:
        abort(404, message=f"News {news_id} not found")

class UsersResource(Resource):
    def get(self, id):
        abort_if_news_not_found(id)
        session = db_session.create_session()
        news = session.query(Users).get(id)
        return jsonify({'users': users.to_dict(
            only=('name', 'about', 'email'))})

    def delete(self, id):
        abort_if_news_not_found(id)
        session = db_session.create_session()
        users = session.query(Users).get(id)
        session.delete(users)
        session.commit()
        return jsonify({'success': 'OK'})


class NewsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        news = session.query(News).all()
        return jsonify({'news': [item.to_dict(
            only=('title', 'content', 'user.name')) for item in news]})

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', required=True)
        parser.add_argument('content', required=True)
        parser.add_argument('is_private', required=True, type=bool)
        parser.add_argument('is_published', required=True, type=bool)
        parser.add_argument('user_id', required=True, type=int)
        args = parser.parse_args()
        session = db_session.create_session()
        news = News(
            title=args['title'],
            content=args['content'],
            user_id=args['user_id'],
            is_published=args['is_published'],
            is_private=args['is_private']
        )
        session.add(news)
        session.commit()
        return jsonify({'success': 'OK'})