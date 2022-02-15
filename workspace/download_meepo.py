#!/usr/bin/python
import requests

def rq_download(url,path,name):
    r = requests.get(url)
    with open(path+name, 'wb') as code:
            code.write(r.content)

if __name__ == '__main__':
    url = 'https://github.com/peerXu/meepo/releases/download/0.7.1/meepo_linux_amd64.tar.gz'
    path = './package/'
    name = 'meepo_linux_amd64.tar.gz'
    rq_download(url, path, name)
