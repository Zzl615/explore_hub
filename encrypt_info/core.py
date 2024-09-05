# -*- encoding: utf-8 -*-
'''
@File    :   core.py
@Time    :   2024/09/05 16:16:45
@Author  :   noaghzil
@Version :   1.0
@Contact :   noaghzil@gmail.com
@Last Modified by  :   noaghzil
@Last Modified time:   2024/09/05 16:16:45
'''

# here put the import lib
from abc import ABC, abstractmethod

class EncryptionBase(ABC):

    @abstractmethod
    def encrypt_data(self, value: str) -> str:
        pass

    @abstractmethod
    def decrypt_data(self, value: str) -> str:
        pass

class BitsEncryption(EncryptionBase):
    """
        位运算加密算法
        # TODO 缺点：
        # 1. 加密过程相对简单，缺乏混淆和扩散
        # 2. 明文和密文之间存在着直接的对应关系，容易被破解
    """

    def encrypt_data(value: str) -> str:
        if not value:
            return value
        try:
            # 将字符串转换为二进制数据
            binary_data = value.encode()
            # 对每个字节进行取反操作
            inverted_data = bytes([~b & 0xFF for b in binary_data])
            # 对取反后的数据进行错一位操作，通过取余保证在0-255范围内
            shifted_data = bytes([(b + 615) % 256 for b in inverted_data])
            # 将取反后的二进制数据转换为十六进制字符串
            return shifted_data.hex()
        except Exception as e:
            print(f"Encryption error: {e}")
            raise e

    def decrypt_data(value: str) -> str:
        if not value:
            return value
        try:
            # 将十六进制字符串转换为二进制数据
            binary_data = bytes.fromhex(value)
            # 对错位后的数据进行反向错位操作，通过取余保证在0-255范围内
            unshifted_data = bytes([(b - 615) % 256 for b in binary_data])
            # 对每个字节再次进行取反操作，恢复原始数据
            original_data = bytes([~b & 0xFF for b in unshifted_data])
            # 将二进制数据解码为字符串
            return original_data.decode()
        except Exception as e:
            print(f"Decryption error: {e}")
            raise e

SECRET_KEY = b'Clol67ZGZpyuZoTO2MJ_qs1G6yShbCX8yvmyGpvDFTA='

class KeyEncryption(EncryptionBase):

    """
      密钥加密算法
      # TODO 缺点：模糊搜索，只支持前缀匹配
    """

    def encrypt_data(value: str) -> str:
        # 加密
        if value and isinstance(value, str):
            try:
                # 将字符串转换为二进制数据
                binary_data = value.encode()
                # 使用XOR运算加密数据
                xored_data = bytes([b ^ SECRET_KEY[i % len(SECRET_KEY)] for i, b in enumerate(binary_data)])
                # 将加密后的二进制数据转换为十六进制字符串
                return xored_data.hex()
            except Exception as e:
                print(e)
        return value

    def decrypt_data(value: str) -> str:
        # 解密
        if value and isinstance(value, str):
            try:
                # 将十六进制字符串转换为二进制数据
                binary_data = bytes.fromhex(value)
                # 使用XOR运算解密数据
                original_data = bytes([b ^ SECRET_KEY[i % len(SECRET_KEY)] for i, b in enumerate(binary_data)])
                # 将二进制数据解码为字符串
                return original_data.decode()
            except (ValueError, UnicodeDecodeError):
                pass
        return value

def encrypt_data(value: str) -> str:
    return BitsEncryption.encrypt_data(value)

def decrypt_data(value: str) -> str:
    return BitsEncryption.decrypt_data(value)
