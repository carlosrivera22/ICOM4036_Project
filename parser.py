from methods import *
from sys import *

def parser(toks):
    style_init = False
    i = 0
    if toks[len(toks)-1][0:3] == "TAG":
        print("Error: Missing \" ")
        raise SystemExit
    if toks[len(toks)-1] == "STYLE":
        print("Error in STYLE: Missing target id parameter")
        raise SystemExit
    while(i < len(toks)):
        if toks[i] == "START" and toks[i+1][0:6] != "STRING":
            print("Error in start command: Missing filename parameter")
            raise SystemExit
        elif "START" not in toks:
            print("Error in start command: Start command not found")
            raise SystemExit
        elif toks[i] + " " + toks[i+1][0:6] == "START STRING":
            create_file(toks[i+1])
            i+=2
        elif toks[i] + " " + toks[i+1] == "ADD FOOTER":
            add_footer()
            i+=2
        elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2][0:6] == "PUT STRING STRING":
            put_content(toks[i+1][8:-1],toks[i+2][8:-1])
            i+=3
        elif toks[i] == "PUT" and toks[i+1][0:6] == "STRING" and toks[i+2][0:6] != "STRING":
            print("Error in put command: Missing parameter")
            raise SystemExit
        elif toks[i] == "PUT" and toks[i+1][0:6] != "STRING":
            print("Error in put command: Missing parameter")
            raise SystemExit
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
        elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2] + " " +toks[i+3][0:6]  == "ADDAFTER STRING GALLERY STRING":
            add_gallery_after(toks[i+1][8:-1], toks[i+3][8:-1])
            i+=4
        elif toks[i] + " " + toks[i+1][0:6] + " " + toks[i+2] + " " +toks[i+3][0:6]  == "ADDINSIDE STRING GALLERY STRING":
            add_gallery_inside(toks[i+1][8:-1], toks[i+3][8:-1])
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
        #ADD ERROR
        elif toks[i] == "ADD" and toks[i+2][0:3] != "TAG":
            print("Error in ADD command: Missing parameter")
            raise SystemExit
        #ADDBEFORE ERROR
        elif toks[i] == "ADDBEFORE" and toks[i+1][0:6] != "STRING":
            print("Error in ADDBEFORE command: Missing target id parameter")
            raise SystemExit
        elif toks[i] == "ADDBEFORE" and toks[i+1][0:6] == "STRING" and toks[i+2][0:3] != "TAG":
            print("Error in ADDBEFORE command: Missing parameter")
            raise SystemExit
        elif toks[i] == "ADDBEFORE" and toks[i+1][0:6] == "STRING" and toks[i+2][0:3] == "TAG" and toks[i+3][0:6] != "STRING":
            print("Error in ADDBEFORE command: Missing id parameter")
            raise SystemExit
        #ADDINSIDE ERROR
        elif toks[i] == "ADDINSIDE" and toks[i+1][0:6] != "STRING":
            print("Error in ADDINSIDE command: Missing target id parameter")
            raise SystemExit
        elif toks[i] == "ADDINSIDE" and toks[i+1][0:6] == "STRING" and toks[i+2][0:3] != "TAG":
            print("Error in ADDINSIDE command: Missing parameter")
            raise SystemExit
        elif toks[i] == "ADDINSIDE" and toks[i+1][0:6] == "STRING" and toks[i+2][0:3] == "TAG" and toks[i+3][0:6] != "STRING":
            print("Error in ADDINSIDE command: Missing id parameter")
            raise SystemExit
        #ADDAFTER ERROR
        elif toks[i] == "ADDAFTER" and toks[i+1][0:6] != "STRING":
            print("Error in ADDAFTER command: Missing target id parameter")
            raise SystemExit
        elif toks[i] == "ADDAFTER" and toks[i+1][0:6] == "STRING" and toks[i+2][0:3] != "TAG":
            print("Error in ADDAFTER command: Missing parameter")
            raise SystemExit
        elif toks[i] == "ADDAFTER" and toks[i+1][0:6] == "STRING" and toks[i+2][0:3] == "TAG" and toks[i+3][0:6] != "STRING":
            print("Error in ADDAFTER command: Missing id parameter")
            raise SystemExit
        elif toks[i] == "STYLE" and toks[i+1][0:6] != "STRING":
            print("Error in STYLE command: Missing target id parameter")
            raise SystemExit
        elif toks[i] == "STYLE" and toks[i+1][0:6] == "STRING" and toks[i+2][0:13] != "STYLE_COMMAND":
            print("Error in STYLE command: Missing style command parameter")
            raise SystemExit
        else:
            i+=1

