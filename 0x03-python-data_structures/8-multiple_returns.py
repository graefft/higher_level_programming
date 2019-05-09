#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        first = None
    else:
        first = sentence[0]

    tup_ret = (len(sentence), first)
    return tup_ret
