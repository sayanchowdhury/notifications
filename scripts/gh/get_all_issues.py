from getpass import getpass
from github3 import login


def login(uname, password):
    return login(uname, password)

def main(uname, password):
    user = login(uname, password)


if __name__ == '__main__':
    uname = input('Github username: ')
    password = getpass('Github password: ')
    main (uname, password)
