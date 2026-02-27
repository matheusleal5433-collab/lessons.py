#operadores logicos
#and (e) or (ou) not (não)
#and - todas as expressões precisam ser verdadeiras para o resultado ser verdadeiro.
#se qualqquer expressão for falsa, o resultado do and é falso.
#a expressão sera avaliada por inteira naquele momento
#sao considerados falsy (quw vc ja viu)
#0 0.0 '' False
#tambem existe o tipo None que e 
#usado para representar um nao valor
#senha_permitida = '1234567'
#if entrada == 'E' and senha_digitavel == senha_permitida:

 #   print('Entrar')
#else:
#    print('Sair')



#avaliação de curto circuito
#quando o resultado de uma expressão logica ja pode ser determinado antes de avaliar todas as express
print(True and False and True) # False
print(bool(0.0)) # False
print(bool(' ')) # True