import requests
import json



def add_ipfs(txt):

    files = {
        'fileOne': (txt),
    }

    response = requests.post('https://ipfs.infura.io:5001/api/v0/add', files=files)
    p = response.json()
    hash = p['Hash']
    return hash


def get_ipfs(hash):
    # retreive
    params = (
        ('arg', hash),
    )
    response_two = requests.post('https://ipfs.infura.io:5001/api/v0/block/get', params=params)
    #print(response_two.text)
    return response_two.text

data = []
def get_list(input):
    hash = add_ipfs(input)
    ipfs_data = get_ipfs(hash)
    data.append(ipfs_data)