import socket
import sys
import base64
import hashlib
import random
import re
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import load_pem_public_key

PASSPHRASE = "user_password"

def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key

def generate_key_aes_gcm():
    key = hashes.Hash(hashes.SHA256(), backend=default_backend())
    key.update(os.urandom(16))
    return key.finalize()

def encrypt_message_aes_gcm(message, key):
    nonce = os.urandom(12)
    algorithm = algorithms.AES(key)
    cipher = Cipher(algorithm, mode=modes.GCM(nonce), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_message = encryptor.update(message) + encryptor.finalize()
    tag = encryptor.tag
    return encrypted_message, tag, nonce

def decrypt_message_aes_gcm(encrypted_message, tag, nonce, key):
    algorithm = algorithms.AES(key)
    cipher = Cipher(algorithm, mode=modes.GCM(nonce, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    return decryptor.update(encrypted_message) + decryptor.finalize()

def send_message(client_socket, message, key):
    encrypted_message, tag, nonce = encrypt_message_aes_gcm(message, key)
    client_socket.sendall(encrypted_message)
    client_socket.sendall(tag)
    client_socket.sendall(nonce)

def receive_message(client_socket, key):
    encrypted_message = client_socket.recv(1024)
    tag = client_socket.recv(16)
    nonce = client_socket.recv(12)
    return decrypt_message_aes_gcm(encrypted_message, tag, nonce, key)

def main():
    global client_socket, client_private_key, client_public_key, key_aes_gcm

    client_socket = socket.socket()
    client_socket.connect(server_address)

    client_private_key, client_public_key = generate_key_pair()

    key_aes_gcm = client_socket.recv(32)

    client_socket.sendall(client_public_key.public_bytes(
        encoding=rsa.serialization.Encoding.PEM,
        format=rsa.serialization.PublicFormat.SubjectPublicKeyInfo
    ))

    client_unique_name = client_socket.recv(1024).decode()

    while True:
        input_messaggio = input()

        if input_messaggio.lower() == "exit":
            break

        send_message(client_socket, input_messaggio, key_aes_gcm)

        decrypted_message = receive_message(client_socket, key_aes_gcm)

        print(decrypted_message)

# Imposta l'indirizzo del server
server_address = ('localhost', 80)

if name == "main":
    main()