    
from core import encrypt_data, decrypt_data

def test_encrypt_decrypt():
    print("========== Test case 1: Normal string ==========\n")
    # Test case 1: Normal string
    original = "Hello, World!"
    encrypted = encrypt_data(original)
    decrypted = decrypt_data(encrypted)
    assert decrypted == original, f"Test case 1 failed: {original} != {decrypted}"
    print(f"Test case 1 passed: {original} == {decrypted}")
    print("------------------------------------")

    print("========== Test case 2: Empty string ==========\n")
    # Test case 2: Empty string
    original = ""
    encrypted = encrypt_data(original)
    decrypted = decrypt_data(encrypted)
    assert decrypted == original, f"Test case 2 failed: {original} != {decrypted}"
    print(f"Test case 2 passed: {original} == {decrypted}")
    print("------------------------------------")

    print("========== Test case 3: String with special characters ==========\n")
    # Test case 3: String with special characters
    original = "!@#$%^&*()_+{}[]|\\:;\"'<>,.?/~`"
    encrypted = encrypt_data(original)
    decrypted = decrypt_data(encrypted)
    assert decrypted == original, f"Test case 3 failed: {original} != {decrypted}"
    print(f"Test case 3 passed: {original} == {decrypted}")
    print("------------------------------------")

    print("========== Test case 4: Long string ==========\n")
    # Test case 4: Long string
    original = "A" * 1000
    encrypted = encrypt_data(original)
    decrypted = decrypt_data(encrypted)
    assert decrypted == original, f"Test case 4 failed: {len(original)} != {len(decrypted)}"
    print(f"Test case 4 passed: length {len(original)} == {len(decrypted)}")
    print("------------------------------------")

    print("========== Test case 5: Unicode characters ==========\n")
    # Test case 5: Unicode characters
    original = "你好，世界！こんにちは、世界！"
    encrypted = encrypt_data(original)
    decrypted = decrypt_data(encrypted)
    assert decrypted == original, f"Test case 5 failed: {original} != {decrypted}"
    print(f"Test case 5 passed: {original} == {decrypted}")
    print("------------------------------------")


    print("========== Test case 6: chr(0～255) ==========\n")
    # Test case 7: chr(0～255)
    original = ""
    for i in range(256):
        original += chr(i)
    encrypted = encrypt_data(original)
    decrypted = decrypt_data(encrypted)
    assert decrypted == original, f"Test case 6 failed: {original} != {decrypted}"
    print(f"Test case 6 passed:")
    print(f"Original: {original}\n\n")
    print(f"Decrypted: {decrypted}\n\n")
    print("*"*10)
    print("Original == Decrypted")
    print("------------------------------------")
    print("------------------------------------")
    print("========== All test cases passed ==========")
    print("All test cases passed successfully!")
    print("------------------------------------")


if __name__ == "__main__":
    test_encrypt_decrypt()