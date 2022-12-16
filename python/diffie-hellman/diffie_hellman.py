import random


def private_key(p):
    return random.randrange(2, p - 1)


def public_key(p, g, private):
    return g ** private % p


def secret(p, public, private):
    return public_key(p, public, private)
