#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        first = None
    else:
        first = len(sentence), sentence[0]

    return first
