from sys import *

tokens = []
symbols = {}

def open_file(filename):
    data = open(filename,"r").read()
    data += "<EOF>"
    return data


