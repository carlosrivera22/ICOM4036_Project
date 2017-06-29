
#methods used in the parser

def create_file(filename):
    filename = "index.html"
    file = open(filename,"w+")
    file.write("<!DOCTYPE html>\n<html>\n<head>\n<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css'>\n<link rel='stylesheet' href='https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css'>\n<script src='https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js'></script>\n</head>\n<title>\n</title>\n<body>\n</body>\n</html>")

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

def add(tag, id, path):
        contents = get_file_contents("index.html")
        index = find_body_index()
        tag = "<" + tag + " id='"+ id + "'>\n" + "</" + tag + "><!-- " + id + "-->\n"
        contents.insert(index,tag)
        write_in_file("index.html",contents)

def add_last(tag,id,path):
        contents = get_file_contents("index.html")
        index = find_closing_body_index()
        if(tag == "img"):
            tag = "<" + tag + " id='"+ id + "' src='" + path + "' ><!-- " + id + "-->\n"
        else:
            tag = "<" + tag + " id='"+ id + "'>\n" + "</" + tag + "><!-- " + id + "-->\n"
        contents.insert(index,tag)
        write_in_file("index.html",contents)

def add_inside(target,tag,id,path):
        contents = get_file_contents("index.html")
        index = find_index_inside(target)
        if(tag == "img"):
            tag = "<" + tag + " id='"+ id + "' src='" + path + "' ><!-- " + id + "-->\n"
        else:
            tag = "<" + tag + " id='"+ id + "'>\n" + "</" + tag + "><!-- " + id + "-->\n"
        contents.insert(index,tag)
        write_in_file("index.html",contents)

def add_before(target,tag,id,path):
        contents = get_file_contents("index.html")
        index = find_index_before(target)
        if(tag == "img"):
            tag = "<" + tag + " id='"+ id + "' src='" + path + "' ><!-- " + id + "-->\n"
        else:
            tag = "<" + tag + " id='"+ id + "'>\n" + "</" + tag + "><!-- " + id + "-->\n"
        contents.insert(index,tag)
        write_in_file("index.html",contents)

def add_after(target,tag,id,path):
        contents = get_file_contents("index.html")
        index = find_index_after(target)
        if(tag == "img"):
            tag = "<" + tag + " id='"+ id + "' src='" + path + "' ><!-- " + id + "-->\n"
        else:
            tag = "<" + tag + " id='"+ id + "'>\n" + "</" + tag + "><!-- " + id + "-->\n"
        contents.insert(index,tag)
        write_in_file("index.html",contents)

def add_bootstrap_after(target,component,id):
        contents = get_file_contents("index.html")
        index = find_index_after(target)
        if(component == "row"):
            tag = "<div id='" + id + "' class='" + component + "'> \n</div><!-- " + id + "-->\n"
        contents.insert(index,tag)
        write_in_file("index.html",contents)

def add_bootstrap_before(target,component,id):
    contents = get_file_contents("index.html")
    index = find_index_before(target)
    if(component == "row"):
        tag = "<div id='" + id + "' class='" + component + "'> \n</div><!-- " + id + "-->\n"
    contents.insert(index,tag)
    write_in_file("index.html",contents)

def add_bootstrap_inside(target,component,id):
    contents = get_file_contents("index.html")
    index = find_index_inside(target)
    tag = "<div id='" + id + "' class='" + component + "'> \n</div><!-- " + id + "-->\n"
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

def get_margin_left(target,margin):
    return "#"+ target + "{" + "margin-left:" + margin[11:] + "}"

def get_margin_right(target,margin):
    return "#"+ target + "{" + "margin-right:" + margin[12:] + "}"

def get_margin_top(target,margin):
    return "#"+ target + "{" + "margin-top:" + margin[10:] + "}"

def get_margin_bottom(target,margin):
    return "#"+ target + "{" + "margin-bottom:" + margin[13:] + "}"

def get_padding_left(target,padding):
    return "#"+ target + "{" + "padding-left:" + padding[12:] + "}"

def get_padding_right(target,padding):
    return "#"+ target + "{" + "padding-right:" + padding[13:] + "}"

def get_padding_top(target,padding):
    return "#"+ target + "{" + "padding-top:" + padding[11:] + "}"

def get_padding_bottom(target,padding):
    return "#"+ target + "{" + "padding-bottom:" + padding[14:] + "}"

def get_height(target,height):
    return "#"+ target + "{" + "height:" + height[7:] + "}"

def get_width(target,width):
    return "#"+ target + "{" + "width:" + width[6:] + "}"

def style(target,style_command,style_type,style_init): #we need to make a list of style commands, validate them depending on the tag...
    if style_init == False:
        add_last("style","mystyle","")
    if style_type == "FONTCOLOR":
        content = get_font_color(target,style_command)
        put_content("mystyle",content)
    elif style_type == "BACKGROUNDCOLOR":
        content = get_background_color(target,style_command)
        put_content("mystyle",content)
    elif style_type == "FONTSIZE":
        content = get_font_size(target,style_command)
        put_content("mystyle",content)
    elif style_type == "MARGINLEFT":
        content = get_margin_left(target,style_command)
        put_content("mystyle",content)
    elif style_type == "MARGINRIGHT":
        content = get_margin_right(target,style_command)
        put_content("mystyle",content)
    elif style_type == "MARGINTOP":
        content = get_margin_top(target,style_command)
        put_content("mystyle",content)
    elif style_type == "MARGINBOTTOM":
        content = get_margin_bottom(target,style_command)
        put_content("mystyle",content)
    elif style_type == "PADDINGBOTTOM":
        content = get_padding_bottom(target,style_command)
        put_content("mystyle",content)
    elif style_type == "PADDINGTOP":
        content = get_padding_top(target,style_command)
        put_content("mystyle",content)
    elif style_type == "PADDINGLEFT":
        content = get_padding_left(target,style_command)
        put_content("mystyle",content)
    elif style_type == "PADDINGRIGHT":
        content = get_padding_right(target,style_command)
        put_content("mystyle",content)
    elif style_type == "WIDTH":
        content = get_width(target,style_command)
        put_content("mystyle",content)
    elif style_type == "HEIGHT":
        content = get_height(target,style_command)
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


# Boostrap Components
# ----------------------
# this fuction adds boostrap jubotron after the element "target" and assigns an id to it
# with title and subtitle
def add_jumbotron_after(target, id, title, subtitle):
    contents = get_file_contents("index.html")
    index = find_index_after(target)
    element = "<div class=\"jumbotron\">\n  <div class=\"container\">\n    <h1>"+title+"</h1>\n    <p>"+subtitle+"</p>\n  </div>\n</div>\n"
    contents.insert(index,element)
    write_in_file("index.html",contents)

def add_jumbotron_before(target, id, title, subtitle):
    contents = get_file_contents("index.html")
    index = find_index_before(target)
    element = "<div class=\"jumbotron\">\n  <div class=\"container\">\n    <h1>"+title+"</h1>\n    <p>"+subtitle+"</p>\n  </div>\n</div>\n"
    contents.insert(index,element)
    write_in_file("index.html",contents)

def add_first_jumbotron(id, title, subtitle):
    contents = get_file_contents("index.html")
    index = find_body_index()
    element = "<div class=\"jumbotron\">\n  <div class=\"container\">\n    <h1>"+title+"</h1>\n    <p>"+subtitle+"</p>\n  </div>\n</div>"
    contents.insert(index,element)
    write_in_file("index.html",contents)

def add_signup_after(target,id):
    contents = get_file_contents("index.html")
    index = find_index_after(target)
    element = "<div class= \"container\">\n  <div class=\"row\">\n    <div class=\"col-sm-6 col-md-offset-3\">\n       <div class=\"well\">\n"
    element+= "<h1>Sign up for Newsletter</h1>\n    <hr>\n    <form action=\"#\">\n    <div class=\"input-group\">\n      "
    element+= "<input style=\"width:320px;\" class=\"btn btn-lg\" name=\"email\" id=\"email\" type=\"email\" placeholder=\"Your Email\" require>\n      "
    element+= "<button class=\"btn btn-info btn-lg\" type=\"submit\">Submit</button>\n    </div>\n    </form>\n"
    element+= "</div>\n    </div>\n  </div>\n</div>"
    contents.insert(index, element)
    write_in_file("index.html", contents)

def add_gallery_after(target,id):
    contents = get_file_contents("index.html")
    index = find_index_after(target)
    element = "<div id='" + id + "'><div class='gallery_product col-lg-4 col-md-4 col-sm-12 col-xs-12 hdpe'><img src='http://fakeimg.pl/365x365/' class='img-responsive'></div>"
    element+= "<div class='gallery_product col-lg-4 col-md-4 col-sm-12 col-xs-12 hdpe'><img src='http://fakeimg.pl/365x365/' class='img-responsive'></div>"
    element+= "<div class='gallery_product col-lg-4 col-md-4 col-sm-12 col-xs-12  hdpe'><img src='http://fakeimg.pl/365x365/' class='img-responsive'></div>" + "</div><!-- " + id + "-->\n"
    contents.insert(index, element)
    write_in_file("index.html", contents)

def add_gallery_inside(target,id):
    contents = get_file_contents("index.html")
    index = find_index_inside(target) + 1
    element = "<br><br><div id='" + id + "'><div class='gallery_product col-lg-4 col-md-4 col-sm-12 col-xs-12 hdpe'><img src='http://fakeimg.pl/365x365/' class='img-responsive'></div>"
    element+= "<div class='gallery_product col-lg-4 col-md-4 col-sm-12 col-xs-12 hdpe'><img src='http://fakeimg.pl/365x365/' class='img-responsive'></div>"
    element+= "<div class='gallery_product col-lg-4 col-md-4 col-sm-12 col-xs-12 hdpe'><img src='http://fakeimg.pl/365x365/' class='img-responsive'></div>" + "</div><!-- " + id + "-->\n"
    contents.insert(index, element)
    write_in_file("index.html", contents)

def add_footer():
    contents = get_file_contents("index.html")
    index = len(contents)-1
    element = "<div class='container-fluid bg-primary py-3'><div class='container'><div class='row py-3'><div class='col-md-9'><p class='text-white'></p></div><div class='col-md-3'>"
    element += "<div class='d-inline-block'><div class='bg-circle-outline d-inline-block'><a href='https://www.facebook.com/' class='text-white'><i class='fa fa-2x fa-fw fa-facebook'></i></a></div>"
    element += "<div class='bg-circle-outline d-inline-block'><a href='https://twitter.com/' class='text-white'><i class='fa fa-2x fa-fw fa-twitter'></i></a></div>"
    element += "<div class='bg-circle-outline d-inline-block'><a href='https://www.linkedin.com/company/' class='text-white'><i class='fa fa-2x fa-fw fa-linkedin'></i></a></div></div></div></div></div></div>"
    contents.insert(index,element)
    write_in_file("index.html", contents)
    print("adding footer..." + str(index))

def add_navbar(sectionsArr):
    if isinstance(sectionsArr, list):
        contents = get_file_contents("index.html")
        index = find_body_index()
        element = "<nav class=\"navbar navbar-default navbar-fixed-top\">\n  <div class=\"container\">\n    <ul class=\"nav navbar-nav\">\n"
        for i in range(len(sectionsArr)):
            if isinstance(sectionsArr[i], list):
                element += "      <li> <a href=\"#"+sectionsArr[i][1]+"\"> "+sectionsArr[i][0]+" </a> </li>\n"
            else:
                raise ValueError('Did not pass a list')
        element +="    </ul>\n  </div>\n</nav>\n"
        contents.insert(index, element)
        write_in_file("index.html",contents)

    else:
        raise ValueError('Did not pass a list')
