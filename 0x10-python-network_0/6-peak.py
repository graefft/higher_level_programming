#!/usr/bin/python3
'''Finds a peak in list'''


def find_peak(list_of_integers):
    '''Finds peak in unsorted list'''
    if not list_of_integers:
        return None

    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]
    if length == 2:
        return max(list_of_integers)

    lo = list_of_integers[mid - 1]
    hi = list_of_integers[mid + 1]
    peak = list_of_integers[mid]

    if peak > lo and peak > hi:
        return peak
    elif peak < lo:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid:])
