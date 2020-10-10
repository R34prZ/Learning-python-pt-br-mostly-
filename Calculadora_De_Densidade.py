#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Calculador de densidade
# d= m/V

        #selecionar grandeza a ser calculada
    
selec_operac = str(input('Você deseja calcular: massa, volume ou densidade? \nOBS:utilize os termos em minúsculo, e certifique-se de que os valores estão no SI '))
        #lista de possíveis grandezas
grandezas = ['massa', 'volume', 'densidade']
#índice         0         1          2
      
        #definindo as possibilidades para cada grandeza 
        
def massa():   
    densidade = float(input('Valor da densidade: '))
    volume = float(input('Valor do volume: '))
    massa = densidade * volume
    print('A massa é de', massa, 'kg')

def volume():
    massa = float(input('Valor da massa: '))
    densidade = float(input('Valor da densidade: '))
    volume = massa / densidade
    print('O volume é de', volume, 'm³')
    
def densidade():
    massa = float(input('Valor da massa: '))
    volume = float(input('Valor do volume: '))
    densidade = massa / volume
    print('A densidade é de', densidade, 'kg/m³')
    
        #mostrando os resultados

if selec_operac == grandezas[0]:
    massa()
    
if selec_operac == grandezas[1]:
    volume()
    
if selec_operac == grandezas[2]:
    densidade()
        

