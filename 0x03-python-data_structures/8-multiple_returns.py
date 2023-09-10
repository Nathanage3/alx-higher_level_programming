#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence:
        return (None)
    else:
        length = len(sentence)
        a = sentence[0]
    return (length, a)
