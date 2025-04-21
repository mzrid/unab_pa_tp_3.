#Importamos la clase Punto() del módulo "Ejercicio_2".
from Ejercicio_2 import Punto

#Creamos la clase Linuea() que recibe como parámetros los objetos Punto creados con la clase Punto().
class Linea():
    def __init__(self,_punto_a,_punto_b):
        self._punto_a = _punto_a;
        self._punto_b = _punto_b;
    
    #Definimos metodos para mover hacia la derecha o izquierda la linea modificando el atributo x de los puntos.
    def mueve_derecha(self, num):
        self._punto_a.x += num
        self._punto_b.x += num
    
    def mueve_izquierda(self, num):
        self._punto_a.x -= num
        self._punto_b.x -= num
    
    #Definimos metodos para mover hacia la arriba o abajo la linea modificando el atributo y de los puntos.
    def mueve_arriba(self, num):
        self._punto_a.y += num
        self._punto_b.y += num
        
    def mueve_abajo(self, num):
        self._punto_a.y -= num
        self._punto_b.y -= num

#Creamos puntos con la clase Punto()
punto1 = Punto(4, 2)
punto2 = Punto(8,4)

#Creamos la linea utilizando como parámetros los puntos definidos
linea1 = Linea(punto1, punto2)

#Utilizamos los métodos para desplazar la linea
linea1.mueve_derecha(2)
linea1.mueve_izquierda(6)
linea1.mueve_arriba(8)
linea1.mueve_abajo(1)

#print(linea1._punto_a.y, linea1._punto_b.y)
        