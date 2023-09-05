"""
@author: Daniela Sanchez

"""

#Diccionarios

diccionario={'Alumno':'Jaime','Edad':'22','Ocupacion':'Ing. en sistemas'}

print("El nombre asignado fue: ",diccionario['Alumno'])


diccionario['Alumno']='Sergio'

print("Ahora con el cambio",diccionario)


del(diccionario['Ocupacion'])

print("Eliminando ocupacion",diccionario)




