"""
@author: Daniela Sanchez

"""

#Funciones

def sumar():
    #num += 20
    print(num)
     
num = 5
sumar()
print(num)


def sumar():
     global num
     num += 20
     
num = 5
sumar()
print(num)


