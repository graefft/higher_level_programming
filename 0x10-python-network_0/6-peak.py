#!/usr/bin/python3
'''Finds a peak in list'''


def find_peak(list_of_integers):
    '''Finds peak in unsorted list'''
    if not list_of_integers:
        return None

    '''check ends'''
    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]
    if length == 2:
        return max(list_of_integers)

    '''compare 1 above & 1 below mid'''
    lo = list_of_integers[mid - 1]
    hi = list_of_integers[mid + 1]
    peak = list_of_integers[mid]

    '''mid is a peak'''
    if peak > lo and peak > hi:
        return peak
    '''lo is higher, make lo new mid'''
    elif peak < lo:
        return find_peak(list_of_integers[:mid])
    '''hi is higher, make hi new mid'''
    else:
        return find_peak(list_of_integers[mid:])
