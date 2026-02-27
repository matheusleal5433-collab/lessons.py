# if / elif / else
# se / se nao se / se nao
entrada = input('Voce quer "entrar" ou "sair"? ')

if entrada == 'entrar':                                 
        print('voce entrou no sistema')
        
        print(21012004) # exemplo de código dentro do bloco do if
elif entrada == 'sair':
    print('voce saiu do sistema')
else:
    print('voce nao digitou nem entrar e nem sair.')
    
print('fora dos blocos')