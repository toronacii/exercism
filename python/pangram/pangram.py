def is_pangram(sentence: str):
    all_letters = set('abcdefghijklmnopqrstuvwxyz')
    set_sentence = set(sentence.lower())
    return all_letters.issubset(set_sentence)
