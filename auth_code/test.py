# -*- encoding: utf-8 -*-
'''
@File    :   test.py
@Time    :   2023/09/05 17:36:08
@Author  :   noaghzil
@Version :   1.0
@Contact :   noaghzil@gmail.com
@Last Modified by  :   noaghzil
@Last Modified time:   2024/09/05 17:36:08
'''

import time
import logging
import unittest
from auth_code.core import Jwt
from jwt import ExpiredSignatureError

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TestJwt(unittest.TestCase):
    def setUp(self):
        self.secret = "fsawads"
        self.ttl = 3600

    def test_jwt_encode_decode(self):
        m_jwt = Jwt(self.secret, self.ttl)
        user_id = 64
        info = m_jwt.generate_user(user_id)
        logger.info(f"Generated JWT: {info}")

        decoded = m_jwt.decode(info)
        logger.info(f"Decoded JWT: {decoded}")

        self.assertEqual(decoded['id'], user_id)
        self.assertEqual(decoded['iss'], 'lab_coat')

    def test_jwt_expiration(self):
        m_jwt = Jwt(self.secret, 0)  # Set TTL to 0 for immediate expiration
        info = m_jwt.generate_user(64)
        logger.info(f"Generated immediately expired JWT: {info}")

        time.sleep(1)  # Wait for 1 second to ensure token expiration

        with self.assertRaises(ExpiredSignatureError):
            m_jwt.decode(info)
        logger.info("ExpiredSignatureError raised as expected")

        decoded = m_jwt.decode(info, verify_exp=False)
        logger.info(f"Decoded expired JWT without expiration verification: {decoded}")
        self.assertEqual(decoded['id'], 64)