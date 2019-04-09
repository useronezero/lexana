keywords = ['auto', 'break', 'case', 'char', 'const', 'continue', 'default', 'do', 'double', 'else', 'enum',
            'extern', 'float', 'for', 'goto', 'if', 'int', 'long', 'register', 'return', 'short',
            'signed', 'sizeof', 'static', 'struct', 'switch', 'typedef', 'union', 'unsigned', 'void', 'volatile',
            'while']
operators = ['+', '-', '/', '%', '++', '--', '==', '!=', '>', '<', '>=', '<=', '&&', '||', '!', '=']
symbols = [',', ';', '(', ')', '{', '}']
symbolTable = {}
symbolTableIndex = 0


def main():
    global symbolTableIndex
    inputStream = input('Please enter the Stream : ')
    i = 0
    while i < len(inputStream):
        if inputStream[i] == ' ' or inputStream[i] == '\t':
            i += 1
            continue
        elif inputStream[i].isalpha():
            i = identifier(i, inputStream)
            continue
        elif inputStream[i].isdigit():
            i = digits(i, inputStream)
            continue
        elif inputStream[i] in operators:
            symbolTable[symbolTableIndex] = {'operator': inputStream[i]}
            symbolTableIndex += 1
        elif inputStream[i] in symbols:
            symbolTable[symbolTableIndex] = {'symbol': inputStream[i]}
            symbolTableIndex += 1
        else:
            pass
        i += 1
    tokenPrint()


def identifier(i, inputStream):
    global symbolTableIndex
    identifier = ''
    while i < len(inputStream):
        if inputStream[i].isalpha() or inputStream[i].isdigit():
            identifier += inputStream[i]
        else:
            break
        i += 1

    if identifier in keywords:
        symbolTable[symbolTableIndex] = {'keyword': identifier}
        symbolTableIndex += 1
    else:
        symbolTable[symbolTableIndex] = {'identifier': identifier}
        symbolTableIndex += 1

    return i


def digits(i, inputStream):
    global symbolTableIndex
    digit = ''
    digitsymbols = '+-'
    while i < len(inputStream):
        if inputStream[i].isdigit():
            digit += inputStream[i]
        elif inputStream[i] == '.':
            try:
                if inputStream[i + 1].isdigit():
                    digit += inputStream[i]
                    i += 1
                    continue
                else:
                    break
            except:
                break
        elif inputStream[i].upper() == 'E':
            try:
                if inputStream[i + 1] in digitsymbols and inputStream[i + 2].isdigit():
                    digit += inputStream[i] + inputStream[i + 1]
                    i += 2
                    continue
                else:
                    break
            except: break
        else:
            break
        i += 1
    if digit != '':
        symbolTable[symbolTableIndex] = {'constant': digit}
        symbolTableIndex += 1
    return i


def tokenPrint():
    for id, token in symbolTable.items():
        for key in token:
            print('< ', key, ', ' + token[key] + ' >')


main()
