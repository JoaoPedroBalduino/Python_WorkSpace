"""Tipos built-in, documentação, tipo imutáveis, métodos de string"""
# https://docs.python.org/pt-br/3/library/stdtypes.html
# Imutável que vimos: str, int, float, bool

string = 'João'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string)
print(outra_variavel)
# Esse codigo mostra o que é necessario para mudar uma variavel imutável


"""Métodos de String (no link a cima)"""
print(string.zfill(10))
print
# >>> 0000000000João 