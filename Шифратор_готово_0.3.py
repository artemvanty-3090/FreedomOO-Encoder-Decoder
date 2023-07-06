import random

def encrypt_message(message):
    encrypted_message = ""
    for letter in message:
        if letter == " ":
            encrypted_message += "2025" + ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(3))
        elif letter == ",":
            encrypted_message += "3025" + ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(3))
        elif letter == "!":
            encrypted_message += "4025" + ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(3))
        elif letter == ".":
            encrypted_message += "5025" + ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(3))
        elif letter == "?":
            encrypted_message += "6025" + ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(3))
        else:
            ascii_code = ord(letter)
            encrypted_message += "{:03d}".format(ascii_code) + ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(3))
            
    return encrypted_message

user_input = input("Введите сообщение на русском языке: ")
encrypted = encrypt_message(user_input)
print("Зашифрованное сообщение:", encrypted)
