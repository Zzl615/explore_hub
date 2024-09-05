# -*- encoding: utf-8 -*-
'''
@File    :   module.py
@Time    :   2024/09/05 16:16:45
@Author  :   noaghzil
@Version :   1.0
@Contact :   noaghzil@gmail.com
@Last Modified by  :   noaghzil
@Last Modified time:   2024/09/05 16:16:45
'''

# here put the import lib

import logging
from tortoise import fields, models
from core import encrypt_data, decrypt_data

logger = logging.getLogger(__name__)

class EncryptedCharField(fields.CharField):
    version = 'v1'
    def to_db_value(self, value, instance):
        try:
            value = encrypt_data(value)
            return f"{self.version}|{value}"
        except Exception as e:
            logger.error(f"Encryption error: {e}")
        return value

    def to_python_value(self, value):
        try:
            _, value = value.split("|")
            return decrypt_data(value)
        except Exception as e:
            pass
        return value

class Patient(models.Model):
    id = fields.IntField(pk=True)
    id_number = EncryptedCharField(max_length=1024, default='')
    name = EncryptedCharField(max_length=1024, default='')
    gender = fields.CharField(max_length=255, default='')
    birthday = fields.DateField(null=True)

    class Meta:
        table = "patient"
        verbose_name = "就诊人信息表"

    # 重写filter方法
    @classmethod
    def filter(cls, *args, **kwargs):
        for key, value in kwargs.items():
            if 'contain' in key and (key.startswith('id_number') or key.startswith('name')):
                kwargs[key] = encrypt_data(value)
        return super().filter(*args, **kwargs)
