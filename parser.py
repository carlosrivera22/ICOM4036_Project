from methods import *

def parser(toks):
    style_init = False
    i = 0
    while(i < len(toks)):
        if toks[i] + " " + toks[i+1][0:6] == "START STRING":
            create_file(toks[i+1])
            i+=2
        elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2][0:6] == "PUT STRING STRING":
            put_content(toks[i+1][8:-1],toks[i+2][8:-1])
            i+=3
        elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2][0:3] + " " + toks[i+3][0:6] == "ADDINSIDE STRING TAG STRING":
            if(toks[i+2][4:] == "img"):
                add_inside(toks[i+1][8:-1],toks[i+2][4:], toks[i+3][8:-1], toks[i+4][8:-1])
                i+=5
            else:
                add_inside(toks[i+1][8:-1],toks[i+2][4:], toks[i+3][8:-1],"")
                i+=4
        elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2][0:3] + " " + toks[i+3][0:6] == "ADDBEFORE STRING TAG STRING":
            if(toks[i+2][4:] == "img"):
                add_before(toks[i+1][8:-1],toks[i+2][4:], toks[i+3][8:-1], toks[i+4][8:-1])
                i+=5
            else:
                add_before(toks[i+1][8:-1],toks[i+2][4:], toks[i+3][8:-1],"")
                i+=4
        elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2][0:3] + " " + toks[i+3][0:6] == "ADDAFTER STRING TAG STRING":
            if(toks[i+2][4:] == "img"):
                add_after(toks[i+1][8:-1],toks[i+2][4:], toks[i+3][8:-1], toks[i+4][8:-1])
                i+=5
            else:
                add_after(toks[i+1][8:-1],toks[i+2][4:], toks[i+3][8:-1],"")
                i+=4
        elif toks[i] + " " + toks[i+1][0:3] + " " + toks[i+2][0:6] == "ADD TAG STRING":
            if(toks[i+1][4:] == "img"):
                add(toks[i+1][4:],toks[i+2][8:-1],toks[i+3][8:-1])
                i+=4
            else:
                add(toks[i+1][4:],toks[i+2][8:-1],"")
                i+=3
        elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2][0:9] + " " + toks[i+3][0:6] == "ADDINSIDE STRING BOOTSTRAP STRING":
            add_bootstrap_inside(toks[i+1][8:-1],toks[i+2][10:], toks[i+3][8:-1])
            i+=4
        elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2][0:9] + " " + toks[i+3][0:6] == "ADDBEFORE STRING BOOTSTRAP STRING":
            add_bootstrap_before(toks[i+1][8:-1],toks[i+2][10:], toks[i+3][8:-1])
            i+=4
        elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2][0:9] + " " + toks[i+3][0:6] == "ADDAFTER STRING BOOTSTRAP STRING":
            add_bootstrap_after(toks[i+1][8:-1],toks[i+2][10:], toks[i+3][8:-1])
            i+=4
        elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2][0:13] == "STYLE STRING STYLE_COMMAND":
            style(toks[i+1][8:-1],toks[i+2][15:-1],toks[i+3],style_init)
            style_init = True
            i+=4
        elif toks[i] + " " + toks[i+1] + " " + toks[i+2][0:6] + " " + toks[i+3][0:6] + " " + toks[i+4][0:6] == "ADD JUMBOTRON STRING STRING STRING":
            add_first_jumbotron(toks[i+2][8:-1], toks[i+3][8:-1], toks[i+4][8:-1])
            i+=5
        elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2] + " " + toks[i+3][0:6] + " " + toks[i+4][0:6] + " " + toks[i+5][0:6] == "ADDAFTER STRING JUMBOTRON STRING STRING STRING":
            add_jumbotron_after(toks[i+1][8:-1], toks[i+3][8:-1],toks[i+4][8:-1], toks[i+5][8:-1])
            i+=6
        elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2] + " " + toks[i+3][0:6] + " " + toks[i+4][0:6] + " " + toks[i+5][0:6] == "ADDBEFORE STRING JUMBOTRON STRING STRING STRING":
            add_jumbotron_before(toks[i+1][8:-1], toks[i+3][8:-1],toks[i+4][8:-1], toks[i+5][8:-1])
            i+=6
        elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2] + " " +toks[i+3][0:6]  == "ADDAFTER STRING SIGNUP STRING":
            add_signup_after(toks[i+1][8:-1], toks[i+3][8:-1])
            i+=4
        elif toks[i] + " " + toks[i+1] == "ADD NAVBAR":
            if toks[i+2] == "OPEN_BRACE":
                comps = list()
                j = 0;
                while toks[i+3+j] != "CLOSE_BRACE":
                    if toks[i+3+j] == "OPEN_BRACKET":
                        innerComps = list()
                    elif toks[i+3+j][0:6] == "STRING":
                        innerComps.append(toks[i+3+j][8:-1])
                    elif toks[i+3+j] == "CLOSE_BRACKET":
                        comps.append(innerComps)
                    j+=1
                add_navbar(comps)
            i+=4+j
        else:
            i+=1
