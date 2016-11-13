import requests

ADDRESS = 'http://172.28.128.3/'

if __name__ == '__main__':
    while True:
        res = requests.get(ADDRESS)
        if res.status_code == 200:
            print('Got 200')
