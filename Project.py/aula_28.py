'''
Iterável -> str, range e etc
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o próximo valor
iter -> me entregue seu iterador 
'''

texto_0 = 'Omega'

for text_1 in texto_0:
    print(text_1)

# Como funciona o "for" por baixo dos panos

texto = 'Omega'
interador =  iter(texto)

while True:
    try: 
        letra = next(interador)
        print(letra)
    except StopIteration:
        break

# É assim que funciona o "for"
