#!/usr/bin/python3
'''Takes in string and sends search request to Star Wars API'''
import requests
import sys


if __name__ == '__main__':
    name = sys.argv[1]
    request = requests.get('https://swapi.co/api/people/?search=' + name)
    response = request.json()
    count = response.get('count')
    print('Number of results: {}'.format(count))
    for i in response.get('results'):
        print(i.get('name'))
    next_page = response.get('next')
    while next_page:
        request = requests.get(next_page)
        response = request.json()
        for i in response.get('results'):
            print(i.get('name'))
        next_page = response.get('next')
