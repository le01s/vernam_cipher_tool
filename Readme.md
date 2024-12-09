# Vernam Cipher Tool

A simple Python implementation of the Vernam cipher, also known as the one-time pad. This script can encrypt and decrypt text files securely using randomly generated keys.

## Features
- Encrypt plain text files.
- Generate unique random keys for each encryption.
- Decrypt encrypted files using saved keys.
- Simple and lightweight.

## How to Use
1. **Encrypt a file:**
   - Place the plain text in `1.txt` (or any other file).
   - Run the script:
     ```bash
     python3 main.py
     ```
   - The key will be saved in `key.txt`.
   - The encrypted message will be saved in `encrypted.txt`.

2. **Decrypt a file:**
   - Run the script with the encrypted file and key:
     ```bash
     python3 main.py
     ```
   - The decrypted message will be saved in `decrypted.txt`.

## Requirements
- Python 3.x

## Notes
- The key is unique for each encryption and must be kept secure.
- Ensure the key file matches the encrypted file for correct decryption.