def hashtag_predeal(file):
    hashls = []
    result = []
    with open(file, 'r') as src:
        lines = src.read().splitlines()
    for line in lines:
        if '#' in line:
            hashls.append(line)
        else:
            result.append(line)

    with open(file, 'w') as temp:
        for line in result:
            temp.write(line+'\n')

    with open("../Hot3nCoder.cpp", 'w') as final:
        for line in hashls:
            final.write(line+'\n')


def normalize(file):
    keyword2ls = ['!=', '%=', '&&', '++', '--', '::', '<<', '<=', '==', '>=', '>>']
    keywordls = ['#', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '[', ']', '{', '}']

    with open(file, 'r') as f:
        src = f.read()

    encodedsrc = []

    i = 0
    while i < len(src):
        temp = src[i:i+2]

        if temp in keyword2ls:
            encodedsrc.append(' ')
            encodedsrc.append(temp)
            encodedsrc.append(' ')
            i += 2
            continue

        if src[i] in keywordls:
            encodedsrc.append(' ')
            encodedsrc.append(src[i])
            encodedsrc.append(' ')
            i += 1
            continue

        encodedsrc.append(src[i])
        i += 1

    result = ''.join(encodedsrc)

    return result
