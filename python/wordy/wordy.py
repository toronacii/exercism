import re


def answer(question: str):
    matches = re.match(
        'What is\s?(-?\d+)?\s?(plus|minus|multiplied by|divided by)?\s?(-?\d+)?\s?(.*)\?', question)

    if not matches:
        raise ValueError('unknown operation')

    n1 = matches[1]
    operation = matches[2]
    n2 = matches[3]
    other_sentence = matches[4]

    if not n1:
        raise ValueError('syntax error')

    if not operation and not n2:
        if other_sentence:
            raise ValueError('unknown operation')
        else:
            return int(n1)

    if (operation and not n2) or (not operation and n2):
        raise ValueError('syntax error')

    if other_sentence:
        n_recursive = answer(f'What is {n1} {operation} {n2}?')
        return answer(f'What is {n_recursive} {other_sentence}?')

    n1 = int(n1)
    n2 = int(n2)

    match operation:
        case 'plus': return n1 + n2
        case 'minus': return n1 - n2
        case 'multiplied by': return n1 * n2
        case 'divided by': return n1 // n2
        case _: raise ValueError('unknown operation')


# SMART SOLUTION

# OPS = {
#     "plus": "__add__",
#     "minus": "__sub__",
#     "multiplied by": "__mul__",
#     "divided by": "__truediv__"
# }


# def answer(question):
#     question = question.removeprefix("What is").removesuffix("?").strip()
#     if not question:
#         raise ValueError("syntax error")
#     if question.isdigit():
#         return int(question)

#     found_op = False
#     for name, op in OPS.items():
#         if name in question:
#             question = question.replace(name, op)
#             found_op = True
#     if not found_op:
#         raise ValueError("unknown operation")

#     ret = question.split()
#     while len(ret) > 1:
#         try:
#             x, op, y, *tail = ret
#             if op not in OPS.values():
#                 raise ValueError("syntax error")
#             ret = [int(x).__getattribute__(op)(int(y)), *tail]
#         except:
#             raise ValueError("syntax error")
#     return ret[0]
