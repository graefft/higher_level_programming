#!/usr/bin/python3
'''Takes in string and sends search request to Star Wars API'''
import requests
import sys


if __name__ == '__main__':
    name = sys.argv[1]
    url = 'https://swapi.co/api/people/?search=' + name
    request = requests.get(url)
    response = request.json()
    count = response.get('count')
    print('Number of results: {}'.format(count))
    for i in response.get('results'):
        print(i.get('name'))
