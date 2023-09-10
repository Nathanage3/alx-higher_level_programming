#!/usr/bin/python3
def multiple_returns(sentence):
    new = ()
    if len(sentence) == 0:
        return (None)
    else:
        length = len(sentence)
        a = sentence[0]
        new = length, a
    return (new)
