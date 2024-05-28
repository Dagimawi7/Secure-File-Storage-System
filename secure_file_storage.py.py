import os
import hashlib

# Derive a key from the password using SHA-256
def derive_key(password: str) -> bytes:
    return hashlib.sha256(password.encode()).digest()

# XOR encryption/decryption
def xor_encrypt_decrypt(data: bytes, key: bytes) -> bytes:
    return bytes(a ^ b for a, b in zip(data, key * (len(data) // len(key)) + key[:len(data) % len(key)]))

# Encrypt a file
def encrypt_file(file_path: str, password: str) -> None:
    key = derive_key(password)
    
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
        
        encrypted_data = xor_encrypt_decrypt(data, key)
        
        with open(file_path + '.enc', 'wb') as f:
            f.write(encrypted_data)
        
        print(f"File '{file_path}' encrypted successfully!")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Decrypt a file
def decrypt_file(file_path: str, password: str) -> None:
    key = derive_key(password)
    
    try:
        with open(file_path, 'rb') as f:
            encrypted_data = f.read()
        
        decrypted_data = xor_encrypt_decrypt(encrypted_data, key)
        
        with open(file_path[:-4], 'wb') as f:
            f.write(decrypted_data)
        
        print(f"File '{file_path}' decrypted successfully!")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function to handle user input
def main():
    while True:
        print("Secure File Storage System")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            file_path = input("Enter the file path to encrypt: ")
            password = input("Enter the password: ")
            encrypt_file(file_path, password)
        elif choice == '2':
            file_path = input("Enter the file path to decrypt: ")
            password = input("Enter the password: ")
            decrypt_file(file_path, password)
        elif choice == '3':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == '__main__':
    main()
