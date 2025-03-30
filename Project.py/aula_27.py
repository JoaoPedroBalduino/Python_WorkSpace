'''
For = Range
range -> range(start, stop, step)
'''
numeros = range(10)
numeros_1 = range(5, 10)
numeros_2 = range (5, 10, 2)
# O ultimo numero não vai ser escrito
#(5, 10, 2)
#(inicio -- limite -- intervalos)S

for numero in numeros:
    print(numero)
