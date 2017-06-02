tokens = []
def lexer(filecontents):
    tok=""
    string=""
    state = 0
    style = ""
    style_state = 0
    style_activate = 0
    filecontents = list(filecontents)
    for char in filecontents:
        tok += char
        if tok == " ": #ignore spaces
            if state == 0:
                tok = ""
        elif tok == "p " or tok == "h1 " or tok == "h2 " or tok == "h3 " or tok == "h4 " or tok == "h5 " or tok == "h6 " or tok == "div " or tok == "img":
            #html tags in here
            tokens.append("TAG:" + tok)
            tok = ""
        elif tok == "\n" or tok == "<EOF>": #what will happen if we reach a new line or the end of the file?
            tok = ""
        elif tok == "START " or tok == "start ":
            tokens.append("START")
            tok = ""
        elif tok == "PUT " or tok == "put ":
            tokens.append("PUT")
            tok = ""
        elif tok == "ADDINSIDE " or tok == "addinside ":
            tokens.append("ADDINSIDE")
            tok = ""
        elif tok == "ADDBEFORE " or tok == "addbefore ":
            tokens.append("ADDBEFORE")
            tok = ""
        elif tok == "ADDAFTER " or tok == "addafter ":
            tokens.append("ADDAFTER")
            tok = ""
        elif tok == "ADDCOMPONENT " or tok == "addcomponent ":
            tokens.append("ADDCOMPONENT")
            tok = ""
        elif tok == "ADD " or tok == "add ":
            tokens.append("ADD")
            tok = ""
        elif tok == "STYLE" or tok == "style ":
            style_activate = 1
            tokens.append("STYLE")
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
        elif (tok == "(" or tok == ")") and style_activate == 1:
            if style_state == 0:
                style_state = 1
            elif style_state == 1:
                style = style + ")"
                tokens.append("STYLE_COMMAND:" + style)
                if style == "(bluetext)" or style == "(redtext)" or style == "(greentext)" or style == "(orangetext)" or style == "(purpletext)" or style == "(whitetext)" or style == "(blacktext)" or style[0:16] + style[-1] == "(customColortext)":
                    tokens.append("FONTCOLOR")
                elif style == "(bluebackground)" or style == "(redbackground)" or style == "(greenbackground)" or style == "(orangebackground)" or style == "(purplebackground)" or style == "(blackbackground)" or style == "(yellowbackground)" or style[0:22] + style[-1] =="(customColorbackground)":
                    tokens.append("BACKGROUNDCOLOR")
                elif style[0:9] + style[-1] == "(fontsize)":
                    tokens.append("FONTSIZE")
                elif style[0:11] + style[-1] == "(marginleft)":
                    tokens.append("MARGINLEFT")
                elif style[0:12] + style[-1] == "(marginright)":
                    tokens.append("MARGINRIGHT")
                elif style[0:10] + style[-1] == "(margintop)":
                    tokens.append("MARGINTOP")
                elif style[0:13] + style[-1] == "(marginbottom)":
                    tokens.append("MARGINBOTTOM")
                elif style[0:12] + style[-1] == "(paddingleft)":
                    tokens.append("PADDINGLEFT")
                elif style[0:13] + style[-1] == "(paddingright)":
                    tokens.append("PADDINGRIGHT")
                elif style[0:11] + style[-1] == "(paddingtop)":
                    tokens.append("PADDINGTOP")
                elif style[0:14] + style[-1] == "(paddingbottom)":
                    tokens.append("PADDINGBOTTOM")
                elif style[0:6] + style[-1] == "(width)":
                    tokens.append("WIDTH")
                elif style[0:7] + style[-1] == "(height)":
                    tokens.append("HEIGHT")
                style = ""
                style_state = 0
                style_activate = 0
                tok = ""
        elif style_state == 1:
            style += tok
            tok = ""


    print(tokens)
    return tokens
