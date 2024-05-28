# Secure-File-Storage-System

Description
The Secure File Storage System is a simple Python-based application that allows users to encrypt and decrypt files using a password. This project demonstrates basic file encryption and decryption using only the Python standard library. The system employs XOR encryption for simplicity and educational purposes.

Features
Encrypt a file: Securely encrypts a file using a password-derived key.
Decrypt a file: Decrypts a previously encrypted file using the same password.
How It Works
Key Derivation: The system derives a 32-byte encryption key from the provided password using SHA-256.
XOR Encryption/Decryption: The system uses XOR encryption to encrypt and decrypt the file contents. While XOR is not secure for real-world applications, it is used here for simplicity.

Prerequisites
Python 3.x installed on your machine.
Project Files
secure_file_storage.py: The main script that handles encryption and decryption.

How to Run
Preparing the Test File
Create a Test File:
Open a text editor and create a new file.
Add some content to the file, for example:
Hello world, as my test.txt 
This is a test file for encryption.
Save the file as test.txt in the same directory as secure_file_storage.py.

Running the Script
Open a Terminal:

Navigate to the directory containing secure_file_storage.py.
Run the Script:

python secure_file_storage.py
Encrypt a File:

Choose option 1 to encrypt a file.
Enter the file path (e.g., test.txt).
Enter a password (e.g., password123).

The script will create an encrypted file named test.txt.enc and display:

File 'test.txt' encrypted successfully!
Decrypt a File:

Choose option 2 to decrypt a file.
Enter the file path of the encrypted file (e.g., test.txt.enc).
Enter the same password used for encryption.

The script will create the decrypted file with the original name (e.g., test.txt) and display:

File 'test.txt.enc' decrypted successfully!

Example Output

Encrypting a File:

Secure File Storage System
1. Encrypt a file
2. Decrypt a file
3. Exit
Enter your choice: 1
Enter the file path to encrypt: test.txt
Enter the password: password123
File 'test.txt' encrypted successfully!

Decrypting a File:

Secure File Storage System
1. Encrypt a file
2. Decrypt a file
3. Exit
Enter your choice: 2
Enter the file path to decrypt: test.txt.enc
Enter the password: password123
File 'test.txt.enc' decrypted successfully!
