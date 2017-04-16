
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
        tag = "<" + tag + " id='"+ id + "'>\n" + "</" + tag + "><!-- " + id + "-->\n"
        contents.insert(index,tag)
        write_in_file("index.html",contents)

def add_last(tag,id):
        contents = get_file_contents("index.html")
        index = find_closing_body_index()
        tag = "<" + tag + " id='"+ id + "'>\n" + "</" + tag + "><!-- " + id + "-->\n"
        contents.insert(index,tag)
        write_in_file("index.html",contents)

def add_inside(target,tag,id):
        contents = get_file_contents("index.html")
        index = find_index_inside(target)
        tag = "<" + tag + " id='"+ id + "'>\n" + "</" + tag + "><!-- " + id + "-->\n"
        contents.insert(index,tag)
        write_in_file("index.html",contents)


def add_before(target,tag,id):
        contents = get_file_contents("index.html")
        index = find_index_before(target)
        tag = "<" + tag + " id='"+ id + "'>\n" + "</" + tag + "><!-- " + id + "-->\n"
        contents.insert(index,tag)
        write_in_file("index.html",contents)

def add_after(target,tag,id):
        contents = get_file_contents("index.html")
        index = find_index_after(target)
        tag = "<" + tag + " id='"+ id + "'>\n" + "</" + tag + "><!-- " + id + "-->\n"
        contents.insert(index,tag)
        write_in_file("index.html",contents)




#todo lo que tenga que ver con styling se puede hacer en una clase aparte



def get_font_color(target,color):
    if(color == "bluetext"):
        return "#"+ target + "{" + "color:blue;" + "}"
    elif(color == "redtext"):
        return "#"+ target + "{" + "color:red;" + "}"
    elif color[0:15] == "customColortext":
        return "#"+ target + "{" + "color:" + color[16:] + "}"

    else:
        print("error") #throw an error when command is invalid

def get_background_color(target,color):
    if(color == "bluebackground"):
        return "#"+ target + "{" + "background-color:blue;" + "}"
    elif color == "redbackground":
        return "#"+ target + "{" + "background-color:red;" + "}"
    elif color[0:21] == "customColorbackground":
        return "#"+ target + "{" + "background-color:" + color[22:] + "}"
    else:
        print("error")

def get_font_size(target,size):
    return "#"+ target + "{" + "font-size:" + size[9:] + "}"

def style(target,style_command,style_type,style_init): #we need to make a list of style commands, validate them depending on the tag...
    if style_init == False:
        add_last("style","mystyle")
    if style_type == "FONTCOLOR":
        content = get_font_color(target,style_command)
        put_content("mystyle",content)
    elif style_type == "BACKGROUNDCOLOR":
        content = get_background_color(target,style_command)
        put_content("mystyle",content)
    elif style_type == "FONTSIZE":
        content = get_font_size(target,style_command)
        put_content("mystyle",content)


def find_index_inside(target):
    target = " id=\'" + target + "\'"
    contents = get_file_contents("index.html")
    i = 0
    while(i < len(contents)):
        if contents[i].find(target) == -1:
            i+=1
        else:
            return i+1
    return False #throw an error

def find_index_before(target):
    target = " id=\'" + target + "\'"
    contents = get_file_contents("index.html")
    i = 0
    while(i < len(contents)):
        if contents[i].find(target) == -1:
            i+=1
        else:
            return i
    return False

def find_index_after(target):
    target = "<!-- " + target + "-->"
    contents = get_file_contents("index.html")
    i = 0
    while(i < len(contents)):
        if contents[i].find(target) == -1:
            i+=1
        else:
            return i+1
    return False

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

def find_closing_body_index():
    contents = get_file_contents("index.html")
    target = "</body>\n"
    i = 0
    while(i < len(contents)):
        if contents[i] == target:
            return i + 1
        i+=1
    return False #throw an error
