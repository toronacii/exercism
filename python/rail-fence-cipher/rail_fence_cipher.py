def _encode(message: str, total_rails: int):
    rs = [[] for _ in range(total_rails)]
    rail, move = 0, 1

    for letter in message:
        rs[rail].append(letter)
        if rail == 0:
            move = 1

        if (rail == total_rails - 1):
            move = -1

        rail += move
    return rs


def encode(message: str, total_rails: int):
    return ''.join([''.join(r) for r in _encode(message, total_rails)])


def decode(message: str, total_rails: int):
    clue = []
    for rail in _encode(range(len(message)), total_rails):
        clue += rail

    d = {}
    for i, k in enumerate(clue):
        d[k] = message[i]

    return ''.join([d[i] for i in range(len(message))])
