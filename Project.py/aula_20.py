"while + while (laços internos)" # Depois da uma olhada como usar o debug


qtd_linhas = 5
qtd_colunas = 5

linha = 1
while linha <= qtd_linhas:
    coluna = 1
    while coluna <= qtd_colunas:
        print(f'{linha=} {coluna=}') # Esse sinal de "=" no f.string: No print vai mostrar o nome da variavel junto com seu valor.
        coluna += 1
    linha += 1

print('Acabou')



