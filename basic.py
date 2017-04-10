from sys import *
import os

tokens = []
symbols = {}

def open_file(filename):
    data = open(filename,"r").read()
    data += "<EOF>"
    return data

def lexer(filecontents):
    tok=""
    string=""
    state = 0
    isexpr = 0
    expr = ""
    n = ""
    varstarted = 0
    var = ""
    filecontents = list(filecontents)
    for char in filecontents:
        tok += char
        if tok == " ": #ignore spaces
            if state == 0:
                tok = ""
        elif tok == "\n" or tok == "<EOF>": #what will happen if we reach a new line or the end of the file?
            if var != "":
                tokens.append("VAR:" + var)
                var = ""
                varstarted = 0
            tok = ""
        elif tok == "START" or tok == "start":
            tokens.append("START")
            tok = ""
        elif tok == "\"" or tok == " \"":
            if state == 0:
                state = 1
            elif state == 1:
                tokens.append("STRING:" + string + "\"")
                string = ""
                state = 0
                tok = ""
        elif state == 1:
            string += tok
            tok = ""

    print(tokens)
    return tokens

def create_file(filename):
    filename = filename[8:-1]
    open(filename,"w")

def parser(toks):
    i = 0
    while(i < len(toks)):
        if toks[i] + " " + toks[i+1][0:6] == "START STRING":
            create_file(toks[i+1])
            i += 2
        i+=1



def run():
    data = open_file(argv[1])
    toks = lexer(data)
    parser(toks)

run()
