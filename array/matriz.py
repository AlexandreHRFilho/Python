def matriz(num_lines,num_columns,value):
    matriz = []
    for i in range(num_columns):
        coluna = []
        for j in range(num_lines):
          coluna.append(value)
        matriz.append(coluna)
    return matriz


def tarefa(mat):
    dim = len(mat)
    for i in range(dim):
        print(mat[i][dim-1-i],end=' ')


def cria_matriz(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(0)
        matriz.append(linha)

    for i in range(num_colunas):
        for j in range(num_linhas):
            matriz[j][i] = int(input("Digite o elemento [" + str(j) + "][" + str(i) + "]: "))

    return matriz
