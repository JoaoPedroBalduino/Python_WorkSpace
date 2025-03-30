'''
Introdução ao try/except
try -> tentar executar o código
except -> ocorreu algum erro ao tentar executar
'''
numero01 = float(input('Digite um número para ele ser dobrado: '))

#numero_float = float(numero) OUTRA POSSIBILIDADE!
print(f'O dobro de {numero01:.0f} é {numero01 * 2:.0f}')

" Outra forma de fazer usando o TRY e o EXCEPT"

numero = input('Digite um número para ele ser dobrado: ')

try:
    numero_float = float(numero)
    print('FLOAT:', numero)
    print(f'O dobro de {numero} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')

'''Acredito que o try e except seja usado em casos que
há uma margem grande de erros vindas pelo usuario de acabar
usando uma variavel que NÃO seja a que deve ser utilizada

Por exemplo: o progama pedi um numero não decimal (2,3,4,6,7)
mas o usuario coloca tipo: (4.6, 2.2, 6.9 ...) ou então 
(a, b, c, fa, dfi, ...)'''


