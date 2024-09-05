# -*- encoding: utf-8 -*-
"""
Module for handling patient data with encryption.

This module defines custom fields and models for storing and retrieving
encrypted patient information using Tortoise ORM.
"""

import logging
from tortoise import fields, models
from encrypt_info.core import encrypt_data, decrypt_data

logger = logging.getLogger(__name__)

class EncryptedCharField(fields.CharField):
    """A custom CharField that encrypts data before saving to the database."""

    VERSION = '1.0.0'

    def to_db_value(self, value, instance):
        """Encrypt the value before saving to the database."""
        if value is None:
            return None
        try:
            encrypted_value = encrypt_data(value)
            return f"{self.VERSION}|{encrypted_value}"
        except Exception as e:
            logger.error(f"Encryption error: {e}")
            return value

    def to_python_value(self, value):
        """Decrypt the value when retrieving from the database."""
        if value is None or '|' not in value:
            return value
        try:
            _, encrypted_value = value.split("|", 1)
            return decrypt_data(encrypted_value)
        except Exception as e:
            logger.error(f"Decryption error: {e}")
            return value

class Patient(models.Model):
    """Model representing a patient with encrypted personal information."""

    id = fields.IntField(pk=True)
    id_number = EncryptedCharField(max_length=1024, default='')
    name = EncryptedCharField(max_length=1024, default='')
    gender = fields.CharField(max_length=255, default='')
    birthday = fields.DateField(null=True)

    class Meta:
        table = "patient"
        verbose_name = "就诊人信息表"

    @classmethod
    def filter(cls, *args, **kwargs):
        """
        Override the filter method to encrypt search parameters for encrypted fields.
        """
        for key, value in kwargs.items():
            if 'contains' in key and key.split('__')[0] in ['id_number', 'name']:
                kwargs[key] = encrypt_data(value)
        return super().filter(*args, **kwargs)
