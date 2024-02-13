"""
@author: Daniela Sanchez

"""

lista = [1, 2, "Hola", 4]

"Juan" in lista #True or False

elemento = "Juan"

#agrega
lista.append(elemento)

otralista=[4, 5, 6]
#agrega Lista
lista.extend(otralista)

index=0
elemento="7"
lista.insert(index,elemento)

#elimina el elemento especificado
lista.remove(elemento)

#elimina el ultimo
lista.pop() 

index=0
#elimina el indice indicado
lista.pop(index) 

elemento = 2
lista.index(elemento)

lista.count(elemento)


