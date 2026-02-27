#operadores logicos
#and (e) or (ou) not (não)
#and - todas as expressões precisam ser verdadeiras para o resultado ser verdadeiro.
#se qualqquer expressão for falsa, o resultado do and é falso.
#a expressão sera avaliada por inteira naquele momento
#sao considerados falsy (quw vc ja viu)
#0 0.0 '' False
#tambem existe o tipo None que e 
#usado para representar um nao valor

'''entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('senha: ')

senha_permitida = '1234567'

if (entrada == 'E' or entrada == 'e' ) and senha_digitada == senha_permitida:
    print('Entrar')
    
else:
    print('Sair')
    
#avaliação de curto circuito'''
print(True or False or 0 or 'abc') 