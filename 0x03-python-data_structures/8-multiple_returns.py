#!/usr/bin/python3

def multiple_returns(sentence):
    ln = len(sentence)
    if ln == 0:
        c = None
    else:
        c = sentence[0]
    tup = (ln, c)
    return tup
