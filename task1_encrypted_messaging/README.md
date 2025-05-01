# Task 1: Encrypted Messaging App Prototype

## Description

This task demonstrates a hybrid encryption scheme:
- **RSA** for public-key encryption of the AES key
- **AES-256** for fast symmetric encryption of the message

## Files

- `message.txt` – original plaintext message
- `encrypted_message.bin` – AES-encrypted message
- `aes_key_encrypted.bin` – AES key encrypted with RSA
- `decrypted_message.txt` – decrypted output
- `userA_private.pem` / `userA_public.pem` – RSA key pair
- `task1_script.py` – Python script implementing the full flow

## Steps

1. Generate RSA key pair.
2. Encrypt a message with AES-256.
3. Encrypt the AES key with RSA public key.
4. Decrypt AES key and use it to decrypt the message.
