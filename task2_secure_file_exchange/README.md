# Task 2: Secure File Exchange Using RSA + AES

## Description

This task demonstrates secure file transmission using a hybrid encryption model:
- **RSA** for securely encrypting the AES key.
- **AES-256 (CBC mode)** for encrypting the file contents.

## Files

- `alice_message.txt` – original message from Alice
- `encrypted_file.bin` – AES-encrypted file with IV prepended
- `aes_key_encrypted.bin` – AES key encrypted using RSA
- `decrypted_message.txt` – recovered file content by Bob
- `public.pem`, `private.pem` – RSA key pair for Bob

## Integrity Check

- SHA-256 hash of original: `533fd80e1be9b0c50c1c4875bc9452713ea9719bc6e64abcd136b46a4b8e7c63`
- SHA-256 hash of decrypted: `533fd80e1be9b0c50c1c4875bc9452713ea9719bc6e64abcd136b46a4b8e7c63`
- ✅ MATCH: Integrity confirmed.

## Steps

1. Bob generates an RSA key pair.
2. Alice writes a message and encrypts it with AES-256.
3. Alice encrypts the AES key using Bob's public key.
4. Bob decrypts the AES key and then the message.
5. Hash comparison verifies the integrity of the decrypted file.
ECHO is on.
