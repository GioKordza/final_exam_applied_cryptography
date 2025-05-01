# Task 4: Email Encryption and Signature Simulation (PGP)

## Description

This task demonstrates the use of digital signatures and encryption for secure email communication.

## Files

- `original_message.txt` – Plaintext message from Alice
- `signed_message.asc` – Signed message with PGP signature block
- `decrypted_message.txt` – Decrypted output (should match original)
- `public.asc`, `private.key` – Simulated PGP key pair for Alice
- `signature_verification.txt` – Explains how the signature is validated

## Steps (Simulated)

1. Alice signs the message using her private key.
2. Bob verifies the message using Alice’s public key.
3. The decrypted content matches the original, confirming authenticity and integrity.

*In real scenarios, tools like GPG or OpenSSL would be used to generate and verify the signature.*
ECHO is on.
