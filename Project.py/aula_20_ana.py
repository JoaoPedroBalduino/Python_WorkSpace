'''Analogia que criei para o estudo do While em While'''

anos_p = int(input('Quantos anos de prisão?; '))
meses_p = int(input('Quantos meses de prisão?; '))

print(f'{anos_p=}')
print(f'{meses_p=}')

anos = 1
while anos <= anos_p:
    meses = 1
    while meses <= meses_p:
        print(f'{anos=}  {meses=}')
        meses += 1
    anos += 1

print('Preso agr está livre!') 