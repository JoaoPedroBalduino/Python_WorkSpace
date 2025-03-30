print('----------------Operadores Logicos----------------')
'''
and (e) or (ou) not (não)

and - Todas as condições precisam ser vedadeiras

Se qualquer valor dor considerado falso a expressão 
inteira será avaliada naquele valor

Tambem existe o tipo None que é usado para 
representar um não valor
'''
entrada = input('[E]ntrada [S]air: ')
senha_digitada = input('Digite a senha: ')

senha_permitida = (123)

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair') 

print('-----------------or-----------------')

s3nha = input('Senha: ') or 'Sem senha'
print(s3nha)