"""
@author: Daniela Sanchez

"""
#herencia y polimorfismo
class figura():
    def __init__(self,nombre,color):
        self.nombre=nombre
        self.color=color
        print("Objeto figura creado")
    def metodo1(self):
        pass
    def area(self):
        print("Metodo area del padre")
        
class rectangulo(figura):
    def __init__(self,nombre,color,arista, vertice):
        super().__init__(nombre ,color)
        self.arista=arista
        self.vertice=vertice
        print("Objeto rectangulo creado")
    def metodo2(self):
        pass
    
    def area(self,b,h):
        print("Metodo area del rectangulo")
        a=b*h
        return a

class circulo(figura):
    def __init__(self,nombre,color,radio, PI):
        super().__init__(nombre,color)
        self.radio=radio
        self.PI=PI
        print("Objeto Circulo creado")
    def metodo3(self):
        pass
    def area(self):
        print("Metodo area del circulo") 
        a=self.radio**2 * self.PI
        return a

figura1=figura("pentagono","verde")
rectangulo1=rectangulo("regular","verde","4","4")
circulo1=circulo("perfecto","rojo",8,3.1416)

figura1.area()
ar=rectangulo1.area(10,5)
print(f"El area del rectangulo es {ar}")
ac=circulo1.area()
print(f"El area del circulo es {ac}")