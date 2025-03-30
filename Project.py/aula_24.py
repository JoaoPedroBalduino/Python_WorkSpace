''' While/iteravel - exercicio'''

frase = str(input('Digite uma frase: '))

index = 0

qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''

while index < len(frase):
    letra_atual = frase[index]

    if letra_atual == ' ':
        index += 1
        continue # Sempre vai procurar o while mais procimo para continuar

    qtd_atual = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes <= qtd_atual:
        qtd_apareceu_mais_vezes = qtd_atual
        letra_apareceu_mais_vezes = letra_atual

    index += 1

print(
    'A letra que apareceu mais vezes foi'
    f'" {letra_apareceu_mais_vezes}" que apareceu'
    f' {qtd_apareceu_mais_vezes}x'
)

