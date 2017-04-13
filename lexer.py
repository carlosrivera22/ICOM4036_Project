tokens = []
def lexer(filecontents):
    tok=""
    string=""
    state = 0
    #istag = 0
    #tag = ""
    #n = ""
    #varstarted = 0
    #var = ""
    filecontents = list(filecontents)
    for char in filecontents:
        tok += char
        if tok == " ": #ignore spaces
            if state == 0:
                tok = ""
        elif tok == " p " or tok == " h1 " or tok == " h2 " or tok == " h3 " or tok == " h4 " or tok == " h5 " or tok == " h6 " or tok == " div ":
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
        elif tok == "STYLE " or tok == "style ":
            tokens.append("STYLE")
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
