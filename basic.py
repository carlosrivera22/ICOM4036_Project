from sys import *

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
    istag = 0
    tag = ""
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
            tok = ""
        elif tok == "START" or tok == "start":
            tokens.append("START")
            tok = ""
        elif tok == "ADDINSIDE" or tok == "addinside":
            tokens.append("ADDINSIDE")
            tok = ""
        elif tok == "ADDBEFORE" or tok == "addbefore":
            tokens.append("ADDBEFORE")
            tok = ""
        elif tok == "ADDAFTER" or tok == "addafter":
            tokens.append("ADDAFTER")
            tok = ""
        elif tok == "ADD " or tok == "add ":
            tokens.append("ADD")
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
    filename = filename[8:-1] + ".html"
    file = open(filename,"w+")
    file.write("<!DOCTYPE html>\n<html>\n<title></title>\n<body>\n</body>\n</html>")

def get_file_contents(filename):
    f = open(filename,"r")
    contents = f.readlines()
    f.close()
    return contents

def write_in_file(filename, contents):
    f = open(filename,"w")
    contents = "".join(contents)
    f.write(contents)
    f.close()

#make a method to get the index of where the tag will be placed

#remember that the tag will be placed after,before or inside another tag...
#maybe change the create command to addinside, addafter and addbefore commands and deal with them separately

def add(tag, id):
    if tag == "p" or tag == "h1" or tag == "h2" or tag == "h3" or tag == "h4" or tag == "h5" or tag == "h6" or tag == "div":
        contents = get_file_contents("index.html")
        index = find_body_index()
        tag = "<" + tag + " id='"+ id + "'>\n" + "</" + tag + ">\n"
        contents.insert(index,tag)
        write_in_file("index.html",contents)
        print(contents)
    else:
        print("not valid tag for inside body")

def add_inside(target,tag,id):
    if tag == "p" or tag == "h1" or tag == "h2" or tag == "h3" or tag == "h4" or tag == "h5" or tag == "h6":
        print("valid tag")
        contents = get_file_contents("index.html")
        index = find_index_inside(target)
        tag = "<" + tag + " id='"+ id + "'>\n" + "</" + tag + ">\n"
        contents.insert(index,tag)
        write_in_file("index.html",contents)
        print(contents)
    else:
        print("not a valid tag") #throw an error

def find_index_inside(target):
    contents = get_file_contents("index.html")
    print(target)
    i = 0
    while(i < len(contents)):
        if contents[i].find(target) == -1:
            i+=1
        else:
            print("found")
            return i+1
    return False #throw an error

def find_body_index():
    contents = get_file_contents("index.html")
    target = "<body>\n"
    print(target)
    i = 0
    while(i < len(contents)):
        if contents[i] == target:
            return i + 1
        i+=1
    return False #throw an error

def parser(toks):
    i = 0
    while(i < len(toks)):
        if toks[i] + " " + toks[i+1][0:6] == "START STRING":
            create_file(toks[i+1])
            i+=2
        elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2][0:6] + " " + toks[i+3][0:6] == "ADDINSIDE STRING STRING STRING":
            add_inside(toks[i+1][8:-1],toks[i+2][8:-1], toks[i+3][8:-1])
            i+=4
        elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2][0:6] == "ADD STRING STRING":
            add(toks[i+1][8:-1],toks[i+2][8:-1])
            i+=3
        if(i == len(toks)):
            i+=1

def run():
    data = open_file(argv[1])
    toks = lexer(data)
    parser(toks)

run()
