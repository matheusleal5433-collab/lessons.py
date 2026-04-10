
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
  
if nome and idade:
    print(f'seu nome é {nome}')
    print(f'seu nome invertido é {nome[::-1]}')
 
    if ' ' in nome:
      print('seu nome contém espaços')
    else:
      print('seu nome não contém espaços')
    
    print(f'seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios.")