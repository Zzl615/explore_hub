import unittest
import logging
from encrypt_info.core import encrypt_data, decrypt_data

logging.basicConfig(level=logging.INFO, format='%(levelname)s - %(message)s')

logger = logging.getLogger(__name__)

class TestEncryptDecrypt(unittest.TestCase):

    def test_normal_string(self):
        original = "Hello, World!"
        logger.info(f"Testing normal string: {original}")
        encrypted = encrypt_data(original)
        logger.info(f"Encrypted: {encrypted}")
        decrypted = decrypt_data(encrypted)
        logger.info(f"Decrypted: {decrypted}")
        logger.info("-" * 40)
        self.assertEqual(decrypted, original)

    def test_empty_string(self):
        original = ""
        logger.info("Testing empty string")
        encrypted = encrypt_data(original)
        logger.info(f"Encrypted: {encrypted}")
        decrypted = decrypt_data(encrypted)
        logger.info(f"Decrypted: {decrypted}")
        logger.info("-" * 40)
        self.assertEqual(decrypted, original)

    def test_special_characters(self):
        original = "!@#$%^&*()_+{}[]|\\:;\"'<>,.?/~`"
        logger.info(f"Testing special characters: {original}")
        encrypted = encrypt_data(original)
        logger.info(f"Encrypted: {encrypted}")
        decrypted = decrypt_data(encrypted)
        logger.info(f"Decrypted: {decrypted}")
        logger.info("-" * 40)
        self.assertEqual(decrypted, original)

    def test_long_string(self):
        original = "A" * 1000
        logger.info(f"Testing long string of length: {len(original)}")
        encrypted = encrypt_data(original)
        logger.info(f"Encrypted length: {len(encrypted)}")
        decrypted = decrypt_data(encrypted)
        logger.info(f"Decrypted length: {len(decrypted)}")
        logger.info("-" * 40)
        self.assertEqual(decrypted, original)

    def test_unicode_characters(self):
        original = "你好，世界！こんにちは、世界！"
        logger.info(f"Testing unicode characters: {original}")
        encrypted = encrypt_data(original)
        logger.info(f"Encrypted: {encrypted}")
        decrypted = decrypt_data(encrypted)
        logger.info(f"Decrypted: {decrypted}")
        logger.info("-" * 40)
        self.assertEqual(decrypted, original)

    def test_all_ascii_characters(self):
        original = ''.join(chr(i) for i in range(256))
        logger.info("Testing all ASCII characters")
        logger.info(f"Original length: {len(original)}")
        encrypted = encrypt_data(original)
        logger.info(f"Encrypted length: {len(encrypted)}")
        decrypted = decrypt_data(encrypted)
        logger.info(f"Decrypted length: {len(decrypted)}")
        logger.info("-" * 40)
        self.assertEqual(decrypted, original)

if __name__ == "__main__":
    unittest.main()