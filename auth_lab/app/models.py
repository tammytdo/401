import base64
from datetime import datetime, timedelta
from hashlib import md5
import json
import os
from time import time
from werkzeug.security import generate_password_hash, check_password_hash
import jwt

from app import db

class Sport(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(256), index = True, unique = True)
    objective = db.Column(db.String(256))
    athletes = db.relationship("Athlete", backref = "sport", lazy = True)

    def to_dict(self):
        return {
                "id": self.id,
                "name": self.name,
                "objective": self.objective,
                "athletes" = [athlete.to_dict() for athlete in self.athletes]
                }

class Athlete(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(256), unique = True)
    recognized_sport = db.Column(db.String(256))
    athlete_id = db.Column(db.Integer, db.ForeignKey("athlete.id"), nullable=True)

    def to_dict(self):
        return {
                "id": self.id, 
                "name": self.name
                "recognized_sport": self.recognized_sport,
                "athlete_id": self.athlete_id
                }

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(140))
    token = db.Column(db.String(32), index=True, unique=True)
    token_expiration = db.Column(db.DateTime)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self, include_email=False):
        data = {
            'id': self.id,
            'username': self.username,
            'about_me': self.about_me,
        }
        if include_email:
            data['email'] = self.email
        return data

    def from_dict(self, data, new_user=False):
        for field in ['username', 'email', 'about_me']:
            if field in data:
                setattr(self, field, data[field])
        if new_user and 'password' in data:
            self.set_password(data['password'])

    def get_token(self, expires_in=3600):
        now = datetime.utcnow()
        if self.token and self.token_expiration > now + timedelta(seconds=60):
            return self.token
        self.token = base64.b64encode(os.urandom(24)).decode('utf-8')
        self.token_expiration = now + timedelta(seconds=expires_in)
        db.session.add(self)
        return self.token

    def revoke_token(self):
        self.token_expiration = datetime.utcnow() - timedelta(seconds=1)

    @staticmethod
    def check_token(token):
        user = User.query.filter_by(token=token).first()
        if user is None or user.token_expiration < datetime.utcnow():
            return None
        return user