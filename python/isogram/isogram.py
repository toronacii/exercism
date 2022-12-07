def is_isogram(string: str):

    if not string.strip():
        return True

    iso: dict = {}
    for char in string.lower():
        if char in 'abcdefghijklmnopqrstuvwxyz':
            if iso.get(char):
                return False

            iso[char] = True

    return True
