from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes

# Generate RSA key pair for User A
key = RSA.generate(2048)
private_key = key.export_key()
public_key = key.publickey().export_key()

with open("userA_private.pem", "wb") as f:
    f.write(private_key)
with open("userA_public.pem", "wb") as f:
    f.write(public_key)

# Create a secret message
message = b"This is a top secret message from User B to User A."
with open("message.txt", "wb") as f:
    f.write(message)

# Encrypt the message with AES
aes_key = get_random_bytes(32)
cipher_aes = AES.new(aes_key, AES.MODE_EAX)
ciphertext, tag = cipher_aes.encrypt_and_digest(message)

with open("encrypted_message.bin", "wb") as f:
    f.write(cipher_aes.nonce + tag + ciphertext)

# Encrypt the AES key using RSA
recipient_key = RSA.import_key(public_key)
cipher_rsa = PKCS1_OAEP.new(recipient_key)
enc_aes_key = cipher_rsa.encrypt(aes_key)

with open("aes_key_encrypted.bin", "wb") as f:
    f.write(enc_aes_key)

# Decrypt AES key and message
cipher_rsa_dec = PKCS1_OAEP.new(RSA.import_key(private_key))
dec_aes_key = cipher_rsa_dec.decrypt(enc_aes_key)

with open("encrypted_message.bin", "rb") as f:
    nonce = f.read(16)
    tag = f.read(16)
    ciphertext = f.read()

cipher_aes_dec = AES.new(dec_aes_key, AES.MODE_EAX, nonce)
decrypted_message = cipher_aes_dec.decrypt_and_verify(ciphertext, tag)

with open("decrypted_message.txt", "wb") as f:
    f.write(decrypted_message)
