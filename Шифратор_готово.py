import random

def encrypt_message(message):
    encrypted_message = ""
    for letter in message:
        ascii_code = ord(letter)
        encrypted_message += "{:03d}".format(ascii_code) + ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(3))
    return encrypted_message

user_input = input("Введите сообщение на русском языке: ")
encrypted = encrypt_message(user_input)
print("Зашифрованное сообщение:", encrypted)