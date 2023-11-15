# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 12:35:30 2023

@author: Daniela
"""

from time import sleep, perf_counter
from threading import Thread

def proceso():
    print('Comenzando...')
    #se define un tiempo "estimado" de 1 segundo
    for i in range(0,11):
        print(f'1 * {i} = {1*i}')
        sleep(1)
    print('Completado \n')

inicio = perf_counter()

#Se crean tres hilos
hilo1 = Thread(target=proceso)
hilo2 = Thread(target=proceso)
hilo3 = Thread(target=proceso)

#Se inician los hilos
hilo1.start()
hilo2.start()
hilo3.start()

#Esperando que se completen los hilos
hilo1.join()
hilo2.join()
hilo3.join()

fin = perf_counter()

tiempoTotal = fin-inicio

print(f'Se tarda {tiempoTotal: 0.2f} segundo(s).')
