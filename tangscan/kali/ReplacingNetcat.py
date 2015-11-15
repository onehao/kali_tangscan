#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
author: Michael <onehao333@gmail.com>



"""
import sys
import socket
import getopt
import threading
import subprocess
# define some global variables
listen = False
command = False
upload = False
execute = ""
target = ""
upload_destination = ""
port = 0