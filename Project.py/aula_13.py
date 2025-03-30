
'''Exercício
    Peça ao usuário para digitar seu nome
    Peça ao usuário para digitar sua idade
    Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é { nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letras}
        A última letra do seu nome é {letra}
    Se nada for digitado em nome ou idade:
    exiba uma mensagem que os campos estao vazios.'''
#-----------------------------------------------------------
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
    
if nome and idade:
   print(f'Seu nome é {nome}')
   print(f'Sua idade é {idade}')
   print(f'Seu nome é invertido é {nome[::-1]}')
   if ' ' in nome:
#  A logica é se(if) espaço(' ') estiver em(in) nome :
       print('Seu nome contém espaços')
   else:
       print('Seu nome NÃO contém espaços')    
       
   print(f'Seu nome é {nome}')
   print(f'Seu nome é {len(nome)}')
   print(f'A primeira letra do seu nome é "{nome[0]}"')
   print(f'A ultima letra do seu nome é "{nome[-1]}"')

else:
    print("Desculpe mas vc deixou espaços vazios")
