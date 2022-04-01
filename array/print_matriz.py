
def imprime_matriz(matriz):
    for i in range(len(matriz)):
        value = f'{matriz[i]}'.replace('[','').replace(']','').replace(',','')
        print(''.join(value))

def sao_multiplicaveis(m1, m2):
    if len(m1[0])==len(m2):
        return True
    else:
        return False
