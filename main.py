import argparse
import os
import sys
from ftplib import FTP

separator = '*****************************************'

# Simple ftp with some useful methods implemented
class CliFtpClient:

    # Core, initialize
    def __init__(self):
        self.ftp = FTP()
        self.ftp.connect('127.0.0.1', 21)
        self.ftp.login('TestUser', '')

    def login(self, user, password):
        self.ftp.login(user, password)

    def dir(self):
        print()
        print('Current FTP directory')
        data = list(self.ftp.mlsd())
        for d in data:
            print('{:10s} {:5s}'.format(d[0], d[1]['type']))
        print(separator)

    def down(self, path):
        self.ftp.cwd(path)

    def up(self):
        self.ftp.cwd('..')


def main():
    ftp = CliFtpClient()
    ftp.ftp.dir()


def ls(path='./'):
    ftp = CliFtpClient()

    # Will print everything to stdout
    ftp.ftp.dir(path)


def upload_to_server(s, d):
    with open(s, 'rb') as f:
        CliFtpClient().ftp.storbinary(f'STOR {d}', f)


def download_from_server(s, d):
    with open(d, 'wb') as f:
        CliFtpClient().ftp.retrbinary(f'RETR {s}', f.write)

if __name__ == '__main__':
    args = sys.argv[1:]
    if args[0] == 'ls':
        print(args[1])
        ls(args[1])
    elif args[0] == 'upload':
        upload_to_server(args[1], args[2])
    elif args[0] == 'download':
        download_from_server(args[1], args[2])
    else:
        print("No way")
