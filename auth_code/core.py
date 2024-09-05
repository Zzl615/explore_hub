# -*- encoding: utf-8 -*-
'''
@File    :   jwt_test.py
@Time    :   2024/09/05 17:25:08
@Author  :   noaghzil
@Version :   1.0
@Contact :   noaghzil@gmail.com
@Last Modified by  :   noaghzil
@Last Modified time:   2024/09/05 17:25:08
'''

# here put the import lib
import jwt
import time


class Jwt:

    def __init__(self, secret: str, ttl: int):
        self.secret = secret
        self.ttl = ttl

    def encode(self, payload: dict):
        return jwt.encode(payload=payload, key=self.secret, algorithm='HS256')

    def decode(self, token: str, verify_exp=True):
        return jwt.decode(jwt=token, key=self.secret, algorithms='HS256', options={'verify_exp': verify_exp})

    def generate_user(self, user_id):
        return self.encode(payload={
            'id': user_id,
            'iss': 'lab_coat',
            'nbf': int(time.time()),
            'iat': int(time.time()),
            'exp': int(time.time()) + self.ttl,
        })
