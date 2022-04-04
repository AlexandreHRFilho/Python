from string import ascii_uppercase
import this
def maiusculas(frase):
    char = ''
    for i in range(len(frase)):
        if frase[i] in ascii_uppercase:
            char += str(frase[i])
    return char

def menor_nome(nomes:list):
    name = []
    for i in nomes:
        name.append(i.strip(' '))
    name = sorted(name, key=len)
    return name[0].capitalize()
