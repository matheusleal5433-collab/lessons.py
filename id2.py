"""
Flag (Bandeira) - Marcar um local
None = Não valor 
is e is not = é ou não é (tipo, valor, identidade)
id = identidade 
"""
condição = False
passou_no_if = None

if condição:
    passou_no_if = True 
    print('Faça algo')
else:
    print('Não faça algo')
 
 
if passou_no_if is None:
     print('nao passou no if')

else:    
#if passou_no_if is not None:
    print('passou no if')
 
 
 
 
 
    
#print(passou_no_if, passou_no_if is None)
#print(passou_no_if, passou_no_if is not None)