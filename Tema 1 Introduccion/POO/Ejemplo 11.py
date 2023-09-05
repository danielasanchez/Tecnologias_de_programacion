"""
@author: Daniela Sanchez

"""

class Perro():
    def __init__(self,**kwargs):
        self.nombre=kwargs.get("nombre")
        self.raza=kwargs.get("raza","Criollo")
        self.edad=kwargs.get("edad")
        self.vacunado=kwargs.get("vacunado",False)
        print("Objeto Creado")
    def vacunar(self):
        self.vacunado=True

perrito1=Perro(nombre="Whisky",edad=11)
print(perrito1.vacunado)
perrito1.vacunar()
print(perrito1.vacunado)






