def parser(toks):
    style_init = False
    i = 0
    while(i < len(toks)):
        if toks[i] + " " + toks[i+1][0:6] == "START STRING":
            create_file(toks[i+1])
            i+=2
        elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2][0:6] == "STYLE STRING STRING":
            print("STYLE SOMETHING...")
            style(toks[i+1][8:-1],toks[i+2][8:-1],style_init)
            style_init = True
            i+=3
        elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2][0:6] == "PUT STRING STRING":
            put_content(toks[i+1][8:-1],toks[i+2][8:-1])
            i+=3
        elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2][0:3] + " " + toks[i+3][0:6] == "ADDINSIDE STRING TAG STRING":
            add_inside(toks[i+1][8:-1],toks[i+2][4:], toks[i+3][8:-1])
            i+=4
        elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2][0:6] == "ADD TAG STRING":
            add(toks[i+1][4:],toks[i+2][8:-1])
            i+=3
        else:
            i+=1

#methods used in the parser

def create_file(filename):
    filename = filename[8:-1] + ".html"
    file = open(filename,"w+")
    file.write("<!DOCTYPE html>\n<html>\n<title>\n</title>\n<body>\n</body>\n</html>")

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

def add(tag, id):
        contents = get_file_contents("index.html")
        index = find_body_index()
        tag = "<" + tag + " id='"+ id + "'>\n" + "</" + tag + ">\n"
        contents.insert(index,tag)
        write_in_file("index.html",contents)


def add_inside(target,tag,id):
        contents = get_file_contents("index.html")
        index = find_index_inside(target)
        tag = "<" + tag + " id='"+ id + "'>\n" + "</" + tag + ">\n"
        contents.insert(index,tag)
        write_in_file("index.html",contents)


#todo lo que tenga que ver con styling se puede hacer en una clase aparte

def get_font_color(target,color):
    if(color == "bluetext"):
        return "#"+ target + "{" + "color:blue;" + "}"
    elif(color == "redtext"):
        return "#"+ target + "{" + "color:red;" + "}"
    else:
        print("error") #throw an error when command is invalid

def style(target,style_command,style_init): #we need to make a list of style commands, validate them depending on the tag...
    if style_init:
        content = get_font_color(target,style_command)
        put_content("mystyle",content)
    else:
        add("style","mystyle")
        content = get_font_color(target,style_command)
        put_content("mystyle",content)


def find_index_inside(target):
    contents = get_file_contents("index.html")

    i = 0
    while(i < len(contents)):
        if contents[i].find(target) == -1:
            i+=1
        else:

            return i+1
    return False #throw an error

def put_content(target,content):
    content = content + "\n"
    contents = get_file_contents("index.html")
    index = find_index_inside(target)
    contents.insert(index,content)
    write_in_file("index.html",contents)

def find_body_index():
    contents = get_file_contents("index.html")
    target = "<body>\n"

    i = 0
    while(i < len(contents)):
        if contents[i] == target:
            return i + 1
        i+=1
    return False #throw an error
