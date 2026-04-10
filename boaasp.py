"""
CONSTANTE = "Variaveis" que nao vao mudar o valor
Muitas condicoes no mesmo if (ruim)
    <-contagem de complexidade (ruim)
"""
velocidade = 61   #Velocidade atual do carro
local_carro = 100 #LOCAL EM QUE O CARRO ESTA NA ESTRADA

RADAR_1 = 60 #velociddade maxima do radar 1
LOCAL_1 = 100 #local onde o radar 1 esta
RADAR_RANGE = 1 #alcance do radar

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) and  \
     local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado_radar_1 = carro_passou_radar_1 and vel_carro_pass_radar_1

if vel_carro_pass_radar_1 :
    print('velocidade carro passou do radar 1')
    
if carro_passou_radar_1:
    print('Carro passou radar 1')
    
if carro_multado_radar_1 :
 print('carro multado em radar 1')
