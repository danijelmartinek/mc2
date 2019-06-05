from flask_pymongo import PyMongo
import datetime

class commonUser:
    def __init__(self, data):
        self.data = data

    def validate(self, collection):
        dataPreset = {
            'email': '',
            'password': '',
            'firstName': '',
            'lastName': '',
            'highSchool': '',
            'address': '',
            'city': '',
            'selectedPath': '',
            'savedPaths': [],
            'role': {
                'roleLevel': 1,
                'roleCaption': ''
            },
            'profilePic': '',
            'createdAt': datetime.datetime.utcnow(),
            'updatedAt': datetime.datetime.utcnow()
        }

        if collection.find_one({'email' : self.data['email']}):
            return {
                'success': False,
                'error': 'Email already exists.'
            }
        
        if not self.data['email']:
            return {
                'success': False,
                'error': 'Email required'
            }
        else:
            dataPreset['email'] = self.data['email']

        if not self.data['password']:
            return {
                'success': False,
                'error': 'Password required'
            }
        else:
            dataPreset['password'] = self.data['password']


        if 'firstName' in self.data:
            dataPreset['firstName'] = self.data['firstName']
        if 'lastName' in self.data:
            dataPreset['lastName'] = self.data['lastName']
        if 'highSchool' in self.data:
            dataPreset['highSchool'] = self.data['highSchool']
        if 'address' in self.data:
            dataPreset['address'] = self.data['address']
        if 'city' in self.data:
            dataPreset['city'] = self.data['city']
        if 'selectedPath' in self.data:
            dataPreset['selectedPath'] = self.data['selectedPath']
        if 'savedPaths' in self.data:
            dataPreset['savedPaths'] = self.data['savedPaths']
        if 'role' in self.data:
            dataPreset['role']['roleLevel'] = self.data['role']['roleLevel']
            dataPreset['role']['roleCaption'] = self.data['role']['roleCaption']
        if 'profilePic' in self.data:
            dataPreset['profilePic'] = self.data['profilePic']

        return {
            'success': True,
            'data': dataPreset
        }

    def save(self, collection):
        res = self.validate(collection)

        if not res['success']:
            return res
        else:
            collection.save(res['data'])
            del res['data']['password']

            return res
