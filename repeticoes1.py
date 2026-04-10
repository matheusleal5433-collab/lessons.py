""" 
repetições1.py  
while (enquanto) 
executa una ação enquanto uma condição for verdadeira
"""

condicao = True

while condicao:
   nome = input('Qual é o seu nome: ')
   print(f'seu nome é {nome}')
   
   if nome == 'sair':
       break # quebra a repetição, interrompe o loop
  
print('acabou')