from sys import *
from lexer import lexer
from parser import parser
import webbrowser
import os
#TO DO:
# LISTA DE STYLE COMMANDS
# AGREGAR COMPONENTES COMO NAVBAR, IMAGENES, TABLAS ENTRE OTROS...


def open_file(filename):
    data = open(filename,"r").read()
    data += "<EOF>"
    return data

def run():
    data = open_file(argv[1])
    toks = lexer(data)
    parser(toks)
    webbrowser.open('file://'+os.path.realpath('index.html'))

run()
