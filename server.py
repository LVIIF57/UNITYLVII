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

ADMIN_PASSPHRASE = "admin_password"
USER_PASSPHRASE = "user_password"

# Dizionario di gruppi e utenti
user_groups = {}

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

def handle_client(client_socket, password):
    global user_groups

    key_aes_gcm = generate_key_aes_gcm()
    client_private_key, client_public_key = generate_key_pair()
    client_unique_name = "USER"

    client_socket.sendall(key_aes_gcm)
    client_socket.sendall(client_public_key.public_bytes(
        encoding=rsa.serialization.Encoding.PEM,
        format=rsa.serialization.PublicFormat.SubjectPublicKeyInfo
    ))

    client_unique_name += f" {roman_numerals(generate_random_number(9999))}"
    client_socket.sendall(client_unique_name.encode())

    while True:
        messaggio Ricevuto = client_socket.recv(1024)
        decrypted_message = decrypt_message_aes_gcm(messaggio Ricevuto, client_socket.recv(16), client_socket.recv(12), key_aes_gcm)
        message_parts = decrypted_message.split()
        command = message_parts[0]
        arguments = message_parts[1:]
if client_unique_name.startswith("ADMIN"):
            if command == "replica":
                send_message(client_socket, f"Ricevuto messaggio da {message_parts[1]} a {message_parts[2]}: {message_parts[3]}", key_aes_gcm)
            elif command == "join":
                if arguments[0] not in user_groups:
                    user_groups[arguments[0]] = set()
                user_groups[arguments[0]].add(client_unique_name)
                send_message(client_socket, f"{client_unique_name} si è unito al gruppo {arguments[0]}.", key_aes_gcm)
            elif command == "crea":
                send_message(client_socket, f"Gruppo {arguments[0]} creato con successo.", key_aes_gcm)
                user_groups[arguments[0]] = set()
            elif command == "bandisci":
                send_message(client_socket, f"Utente {arguments[0]} bandito da {arguments[1]}.", key_aes_gcm)
                try:
                    user_groups[arguments[1]].remove(user_groups[arguments[0]])
                except KeyError:
                    send_message(client_socket, f"Utente {arguments[1]} non trovato.", key_aes_gcm)
            elif command == "muta":
                send_message(client_socket, f"Utente {arguments[0]} mutato in {arguments[1]}.", key_aes_gcm)
                user_groups[arguments[1]] = user_groups.pop(arguments[0], None)
            elif command == "messaggio":
                send_message(client_socket, f"Messaggio inviato da {client_unique_name} a {message_parts[1]}: {message_parts[2]}", key_aes_gcm)
            elif command == "kick":
                send_message(client_socket, f"Utente {arguments[0]} è stato rimosso dal gruppo {arguments[1]} dal supervisore.", key_aes_gcm)
                try:
                    user_groups[arguments[1]].remove(user_groups[arguments[0]])
                except KeyError:
                    send_message(client_socket, f"Utente {arguments[1]} non trovato.", key_aes_gcm)
        else:
            send_message(client_socket, f"Comando non riconosciuto per {client_unique_name}", key_aes_gcm)

# Avvia il server
print(f"Server avviato. Indirizzo: localhost, Porta: 80, Numero: {server_number}")
server_socket = socket.socket()
server_socket.bind(("localhost", 80))
server_socket.listen(5)
while True:
    client_socket, client_address = server_socket.accept()
    password = input("Inserisci la password di accesso: ")
    Thread(target=handle_client, args=(client_socket, password)).start()
