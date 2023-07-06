def decipher(input_string):
    russian_string = ''.join(char for char in input_string if not char.isalpha() or char.isalpha() and not char.isascii())
    parts = [russian_string[i:i+4] for i in range(0, len(russian_string), 4)]
    result = ''
    for part in parts:
        ascii_code = int(part)
        if ascii_code == 2025:
            result += ' '
        elif ascii_code == 3025:
            result += ','
        else:
            result += chr(ascii_code)

    return result
input_string = input("Введите зашифрованную строку: ")
deciphered_string = decipher(input_string)
print("Расшифрованная строка:", deciphered_string)
