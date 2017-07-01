from sys import *

from lexer import lexer

from parser import parser

from methods import create_file



import webbrowser

import os






def open_file(filename):

    data = open(filename,"r").read()

    data += "<EOF>"

    return data



def run():

    data = open_file(argv[1])

    toks = lexer(data)

    parser(toks)

    webbrowser.open('file://'+os.path.realpath(create_file.HTML_FILE))



run()