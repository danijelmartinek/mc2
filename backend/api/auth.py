from flask import session, json, jsonify
from flask_redis import FlaskRedis
from flask_session import Session
from bson import ObjectId
import hashlib, binascii, os, sys, datetime, time

from models.user import commonUser
sys.path.append("..")


class JSONEncoder(json.JSONEncoder):  #klasa za pretvorbu Mongo objekata u string
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        elif isinstance(o, datetime.datetime):
            return o.isoformat()
        elif isinstance(o, datetime.date):
            return o.isoformat()
        elif isinstance(o, datetime.timedelta):
            return (datetime.datetime.min + o).time().isoformat()
        else:
            return json.JSONEncoder.default(self, o)





class Auth:
    def __init__(self, app):
        self.app = app

    def init(self, sessionLifetime):
        self.app.config["SESSION_TYPE"] = 'redis'
        self.app.config["SECRET_KEY"] = os.urandom(24)
        self.app.config["PERMANENT_SESSION_LIFETIME"] = sessionLifetime
        Session(self.app)

        
    def setSession(self, userData):
        session['sessionUser'] = userData
        return {'auth': True, 'userData': json.loads(userData)}

    def getSession(self):
        data = session.get('sessionUser')

        if data:
            return jsonify({'auth': True, 'userData': json.loads(data)})
        else:
            return jsonify({'auth': False})

    def clearSession(self):
        session.clear()
        return jsonify({'authCleared': True})





class SignUp:
    def __init__(self, session, dbCollection):
        self.session = session
        self.dbCollection = dbCollection
    
    def registerUser(self, data):
        if not data['email']:
            return {
                'success': False,
                'error': 'Email required'
            }
        if not data['password']:
            return {
                'success': False,
                'error': 'Password required'
            }

        data['password'] = self.hash_password(data['password'])
        savedUser = commonUser(data).save(self.dbCollection)
        if not savedUser['success']:
            return savedUser
        
        self.session.clearSession()
        registeredUser = JSONEncoder().encode(savedUser['data'])
        
        return self.session.setSession(registeredUser)


    def loginUser(self, data):
        if not data['email']:
            return {
                'success': False,
                'error': 'Email required.'
            }
        if not data['password']:
            return {
                'success': False,
                'error': 'Password required.'
            }

        user = self.dbCollection.find_one({'email' : data['email']})

        if self.verify_password(user['password'], data['password']):
            self.session.clearSession()
            del user['password']
            loggedUser = JSONEncoder().encode(user)
            return self.session.setSession(loggedUser)
        else:
            return {
                'success': False,
                'error': 'Passwords does not match.'
            }



    def hash_password(self, password):

        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
        pwdhash = binascii.hexlify(pwdhash)
        return (salt + pwdhash).decode('ascii')


    def verify_password(self, stored_password, provided_password):

        salt = stored_password[:64]
        stored_password = stored_password[64:]
        pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        return pwdhash == stored_password
