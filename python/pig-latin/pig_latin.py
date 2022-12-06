import re


def translate_word(word: str):
    match_vowel = re.match('xr|yt|[aeiou]', word)
    if match_vowel:
        return word + 'ay'

    match_consonant = re.match(
        '(thr|sch|th|ch|qu|rh|[bcdfghjklmnpqrstvwxyz])(qu)?(y)?(.+)', word)

    if match_consonant:
        cluster, qu, y, rest = match_consonant.groups()

        return ''.join(filter(None, (y, rest, cluster, qu, 'ay')))

    return word


def translate(text: str):
    return ' '.join(map(translate_word, text.split(' ')))
