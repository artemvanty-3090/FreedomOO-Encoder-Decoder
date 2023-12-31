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
        elif ascii_code == 4025:
            result += '!'
        elif ascii_code == 5025:
            result += '.'
        elif ascii_code == 6025:
            result += '?'
        elif ascii_code == 7025:
            result += '@'
        elif ascii_code == 8025:
            result += '#'
        elif ascii_code == 9025:
            result += '№'
        elif ascii_code == 1026:
            result += '$'
        elif ascii_code == 2026:
            result += ';'
        elif ascii_code == 3026:
            result += '%'
        elif ascii_code == 4026:
            result += '^'
        elif ascii_code == 5026:
            result += ':'
        elif ascii_code == 6026:
            result += '&'
        elif ascii_code == 7026:
            result += '*'
        elif ascii_code == 8026:
            result += '('
        elif ascii_code == 9026:
            result += ')'
        elif ascii_code == 1027:
            result += '-'
        elif ascii_code == 2027:
            result += '+'
        elif ascii_code == 3027:
            result += '='
        elif ascii_code == 4027:
            result += '<'
        elif ascii_code == 5027:
            result += '>'
        elif ascii_code == 6027:
            result += '"'
        elif ascii_code == 7027:
            result += '/'
        elif ascii_code == 8027:
            result += '|'
        else:
            result += chr(ascii_code)

    return result
input_string = input("Введите зашифрованную строку: ")
deciphered_string = decipher(input_string)
print("Расшифрованная строка:", deciphered_string)