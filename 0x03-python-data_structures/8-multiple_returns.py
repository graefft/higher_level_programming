#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        first = (0, None)
    else:
        first = (len(sentence), sentence[0])
    return first
