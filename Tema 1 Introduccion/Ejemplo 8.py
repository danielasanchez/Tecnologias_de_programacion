"""
@author: Daniela Sanchez

"""
s1 = "Cadena 1"

s2 = "Cadena 2" 

mensaje = s1 + " " +s2

print ("El mensaje: '{}' tiene como longitud {} caracteres".format(mensaje,len(mensaje)))

print("Esta es la {} y esta la {}".format(s1,s2))

print("Esta es la {1} y esta la {0}".format(s1,s2))

print("Esta es la {v1} y esta la {v2}".format(v1=s1,v2=s2))

print(f"Aqui se imprime como cadena N1 {s1} + N2 {s2}")
