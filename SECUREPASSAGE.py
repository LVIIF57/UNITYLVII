import socket
import socks
import getpass
import sys
import os
import base64
import hashlib
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256

def get_fixed_key():
    key = b'0123456789abcdef0123456789abcdef'  # 256-bit AES/GCM key
    return key

def encrypt_key(key, salt, password):
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_key = encryptor.update(salt) + encryptor.finalize()
    encrypted_key_base64 = base64.b64encode(encrypted_key).decode()
    return encrypted_key_base64

def decrypt_key(encrypted_key_base64, password):
    encrypted_key = base64.b64decode(encrypted_key_base64.encode())
    cipher = Cipher(algorithms.AES(password), modes.ECB(), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_key = decryptor.update(encrypted_key) + decryptor.finalize()
    return decrypted_key

def connect_to_server(server_address, server_port, tor_port):
    socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", tor_port)
    socket.socket = socks.socksocket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((server_address, server_port))
    return client_socket

def send_message(client_socket, message):
    encrypted_message_bytes = encrypt_message(message)
    client_socket.sendall(encrypted_message_bytes)

def receive_message(client_socket):
    encrypted_received_bytes = client_socket.recv(1024)
    received_message = decrypt_message(encrypted_received_bytes)
    return received_message

def encrypt_message(message):
    encrypted_message = encryptor.update(message.encode()) + encryptor.finalize()
    encrypted_message_bytes = base64.b64encode(encrypted_message)
    return encrypted_message_bytes

def decrypt_message(encrypted_message_bytes):
    decrypted_message = decryptor.update(base64.b64decode(encrypted_message_bytes)) + decryptor.finalize()
    return decrypted_message.decode()

def setup_encryption(key):
    nonce = os.urandom(12)
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
    encryptor = cipher.encryptor()
    decryptor = cipher.decryptor()
    return encryptor, decryptor

def main():
    if len(sys.argv) != 5:
        print("Usage: python client.py <server_address> <server_port> <tor_port> <password>")
        sys.exit(1)

    server_address = sys.argv[1]
    server_port = int(sys.argv[2])
    tor_port = int(sys.argv[3])
    password = sys.argv[4].encode()

    key = get_fixed_key()
    encrypted_key = encrypt_key(key, os.urandom(16), password)
    client_socket = connect_to_server(server_address, server_port, tor_port)
    client_socket.sendall(encrypted_key.encode())

    encryptor, decryptor = setup_encryption(key)

    print("[Inizio sessione di chat]")
    while True:
        input_message = input("Utente (UNITY-{0}): ".format(get_roman_number()))
        if input_message.lower() == "exit":
            break
        send_message(client_socket, input_message)
        received_message = receive_message(client_socket)
        print("[Messaggio ricevuto dal server: " + received_message + "]")

    client_socket.close()

def get_roman_number():
    number = random.randint(1, 10)
    roman_numeral = roman_numerals(number)
    return roman_numeral

def roman_numerals(num):
    if num > 999:
        print("Il numero deve essere inferiore a 1000 per generare numeri romani.")
        return
    if num < 1:
        print("Il numero deve essere maggiore o uguale a 1 per generare numeri romani.")
        return
    if num == 1:
        return "I"
    if num == 2:
        return "II"
    if num == 3:
        return "III"
    if num == 4:
        return "IV"
    if num == 5:
        return "V"
    if num == 6:
        return "VI"
    if num == 7:
        return "VII"
    if num == 8:
        return "VIII"
    if num == 9:
        return "IX"
    if num == 10:
        return "X"
    if num == 40:
        return "XL"
    if num == 50:
        return "L"
    if num == 90:
        return "XC"
    if num < 100:
        if num % 10 == 0:
            return roman_numerals(num // 10) + "X"
        elif num % 10 == 1:
            return roman_numerals(num // 10) + "X" + roman_numerals(1)
        elif num % 10 == 2:
            return roman_numerals(num // 10) + "X" + roman_numerals(2)
        elif num % 10 == 3:
            return roman_numerals(num // 10) + "X" + roman_numerals(3)
        elif num % 10 == 4:
            return roman_numerals(num // 10) + "X" + roman_numerals(4)
        elif num % 10 == 5:
            return roman_numerals(num // 10) + "X" + roman_numerals(5)
        elif num % 10 == 6:
            return roman_numerals(num // 10) + "X" + roman_numerals(6)
        elif num % 10 == 7:
            return roman_numerals(num // 10) + "X" + roman_numerals(7)
        elif num % 10 == 8:
            return roman_numerals(num // 10) + "X" + roman_numerals(8)
        elif num % 10 == 9:
            return roman_numerals(num // 10) + "X" + roman_numerals(9)
    elif num < 1000:
        if num % 100 == 0:
            return roman_numerals(num // 100) + "C"
        elif num % 100 == 10:
            return roman_numerals(num // 100) + "C" + "X"
        elif num % 100 == 20:
            return roman_numerals(num // 100) + "C" + "X" + "X"
        elif num % 100 == 30:
            return roman_numerals(num // 100) + "C" + "X" + "X" + "X"
        elif num % 100 == 40:
            return roman_numerals(num // 100) + "C" + "X" + roman_numerals(4)
        elif num % 100 == 50:
            return roman_numerals(num // 100) + "C" + "L"
        elif num % 100 == 60:
            return roman_numerals(num // 100) + "C" + "L" + "X"
        elif num % 100 == 70:
            return roman_numerals(num // 100) + "C" + "L" + "X" + "X"
        elif num % 100 == 80:
            return roman_numerals(num // 100) + "C" + "L" + "X" + "X" + "X"
        elif num % 100 == 90:
            return roman_numerals(num // 100) + "C" + "L" + "X" + roman_numerals(9)
    else:
        return
