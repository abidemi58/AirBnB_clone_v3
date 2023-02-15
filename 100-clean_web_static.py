#!/usr/bin/python3
""" Function that deploys """
from fabric.api import *


env.hosts = ["54.145.240.183", "35.153.57.197"]
env.user = "ubuntu"


def do_clean(number=0):
    """
    cleans
    """

    number = int(number)

    if number == 0:
        numbers = 1
    else:
        numbers = number

    local('cd versions ; ls -t | head -n -{} | xargs rm -rf'.format(numbers))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | head -n -{} | xargs rm -rf'.format(path, numbers))
