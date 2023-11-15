# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 12:35:30 2023

@author: Daniela
"""

#Llamado común del llamado de una función múltiple veces
from time import sleep, perf_counter

def proceso():
    print('Comenzando...')
    #se define un tiempo "estimado" de 1 segundo
    for i in range(0,11):
        print(f'1 * {i} = {1*i}')
        sleep(1)
    print('Completado \n')

#perf_counter regresa el tiempo en segundos
inicio = perf_counter()

#llama la función proceso() 3 veces
proceso()
proceso()
proceso()

fin = perf_counter()

tiempoTotal = fin-inicio

print(f'Se tarda {tiempoTotal: 0.2f} segundo(s).')
