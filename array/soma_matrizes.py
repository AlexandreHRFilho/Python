
def soma_matrizes(m1,m2):
    matriz = []

    if (len(m1) == len(m2)) and (len(m1[0]) == len(m2[0])):
        for i in range(len(m1)):
            linha = []
            for j in range(len(m1[0])):
                linha.append(m1[i][j]+ m2[i][j])
            matriz.append(linha)
        return matriz
    else:
        return False

