# -*- encoding: utf-8 -*-
"""
@File    :   core.py
@Time    :   2024/09/05 16:16:45
@Author  :   noaghzil
@Version :   1.0
@Contact :   noaghzil@gmail.com
@Last Modified by  :   noaghzil
@Last Modified time:   2024/09/05 16:16:45
"""

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
    优点：
    1. 实现简单：使用基本的位运算，易于理解和实现
    2. 计算速度快：位运算操作效率高，适合大量数据的快速加密
    3. 无需额外的库支持：可以直接使用语言内置的位运算操作
    4. 可逆性：通过相同的位运算可以轻松解密

    缺点：
    1. 加密强度低：加密过程相对简单，缺乏复杂的混淆和扩散
    2. 易于破解：明文和密文之间存在直接的对应关系，容易被分析和破解
    3. 不适合敏感数据：由于安全性较低，不适合用于加密高度敏感的信息
    4. 缺乏随机性：加密结果具有确定性，相同的输入总是产生相同的输出
    5. 无法抵抗统计分析：频率分析等统计方法可能会破解加密内容
    6. 密钥管理问题：通常使用固定的位移量，缺乏灵活的密钥管理机制
    """

    @staticmethod
    def encrypt_data(value: str) -> str:
        if not value:
            return value
        try:
            binary_data = value.encode()
            shifted_data = bytes([(b + 615) % 256 for b in binary_data])
            return shifted_data.hex()
        except Exception as e:
            print(f"Encryption error: {e}")
            raise

    @staticmethod
    def decrypt_data(value: str) -> str:
        if not value:
            return value
        try:
            binary_data = bytes.fromhex(value)
            original_data = bytes([(b - 615) % 256 for b in binary_data])
            return original_data.decode()
        except Exception as e:
            print(f"Decryption error: {e}")
            raise

SECRET_KEY = b'1234567890'

class KeyEncryption(EncryptionBase):
    """
    密钥加密算法
    优点：
    1. 安全性较高：使用密钥进行加密，增加了破解难度
    2. 可逆性：可以通过密钥进行解密，恢复原始数据
    3. 实现简单：XOR运算易于实现，计算速度快

    缺点：
    1. 模糊搜索能力有限：只支持前缀匹配，无法进行全文搜索
    2. 密钥管理：需要安全地存储和管理密钥，密钥泄露会导致安全风险
    3. 固定密钥：使用固定密钥可能导致模式分析攻击
    4. 长度泄露：加密后的数据长度与原始数据相同，可能泄露信息
    5. 缺乏完整性验证：无法检测数据是否被篡改
    """

    @staticmethod
    def encrypt_data(value: str) -> str:
        if not value or not isinstance(value, str):
            return value
        try:
            binary_data = value.encode()
            xored_data = bytes([b ^ SECRET_KEY[i % len(SECRET_KEY)] for i, b in enumerate(binary_data)])
            return xored_data.hex()
        except Exception as e:
            print(f"Encryption error: {e}")
            return value

    @staticmethod
    def decrypt_data(value: str) -> str:
        if not value or not isinstance(value, str):
            return value
        try:
            binary_data = bytes.fromhex(value)
            original_data = bytes([b ^ SECRET_KEY[i % len(SECRET_KEY)] for i, b in enumerate(binary_data)])
            return original_data.decode()
        except (ValueError, UnicodeDecodeError) as e:
            print(f"Decryption error: {e}")
            return value

def encrypt_data(value: str) -> str:
    return BitsEncryption.encrypt_data(value)

def decrypt_data(value: str) -> str:
    return BitsEncryption.decrypt_data(value)
