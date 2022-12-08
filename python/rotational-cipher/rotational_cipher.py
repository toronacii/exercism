ALPHABETH = 'abcdefghijklmnopqrstuvwxyz'


def rotate(text: str, key: int):
    cipher_alpha = ALPHABETH[key:] + ALPHABETH[:key]

    cipher_text = ''
    for char in text:
        if char.lower() in ALPHABETH:
            index = ALPHABETH.index(char.lower())
            newChar = cipher_alpha[index]
            cipher_text += newChar if char == char.lower() else newChar.upper()
        else:
            cipher_text += char

    return cipher_text
