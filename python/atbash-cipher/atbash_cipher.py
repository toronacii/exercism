ALPHA = '0123456789abcdefghijklmnopqrstuvwxyz9876543210'


def convert(text: str):
    txt = ''.join([
        char
        for char in text.lower()
        if char in ALPHA
    ])

    translation = txt.maketrans(ALPHA, ALPHA[::-1])

    return txt.translate(translation).strip()


def encode(plain_text: str):
    translation = convert(plain_text)

    result = ''

    for i, char in enumerate(translation, start=0):
        if i % 5 == 0:
            result += ' '
        result += char

    return result.strip()


def decode(ciphered_text: str):
    return convert(ciphered_text)
