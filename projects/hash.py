def encrypt(plaintext, key):
    # Convert characters to numerical values (A=0, B=1, ..., Z=25)
    plaintext_numbers = [ord(char) - ord('A') for char in plaintext.upper()]
    key_numbers = [ord(char) - ord('A') for char in key.upper()]

    ciphertext_numbers = []
    key_length = len(key_numbers)

    # Encrypt each character
    for i in range(len(plaintext_numbers)):
        # Apply the encryption formula
        encrypted_value = (plaintext_numbers[i] + key_numbers[i % key_length]) % 26
        ciphertext_numbers.append(encrypted_value)

    # Convert numerical values back to characters
    ciphertext = ''.join(chr(num + ord('A')) for num in ciphertext_numbers)
    return ciphertext

def decrypt(ciphertext, key):
    # Convert characters to numerical values (A=0, B=1, ..., Z=25)
    ciphertext_numbers = [ord(char) - ord('A') for char in ciphertext.upper()]
    key_numbers = [ord(char) - ord('A') for char in key.upper()]

    plaintext_numbers = []
    key_length = len(key_numbers)

    # Decrypt each character
    for i in range(len(ciphertext_numbers)):
        # Apply the decryption formula
        decrypted_value = (ciphertext_numbers[i] - key_numbers[i % key_length]) % 26
        plaintext_numbers.append(decrypted_value)

    # Convert numerical values back to characters
    plaintext = ''.join(chr(num + ord('A')) for num in plaintext_numbers)
    return plaintext

# Example usage of the decryption function
# ciphertext = "RIJVS"
# key = "KEY"
# decrypted_text = decrypt(ciphertext, key)
# print(f"Decrypted Text: {decrypted_text}")

# Example usage
plaintext = input("input password to hash: ")
key = input("input the key to use: ")
ciphertext = encrypt(plaintext, key)
print(f"Ciphertext: {ciphertext}")
print(f'⚠️Please store the key:{key} in a safe location.')
