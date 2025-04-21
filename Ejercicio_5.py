#Creamos la clase Persona con atributos nombre y apellido
class Persona():
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    #Definimos un método str donde se va a mostrar el nombre y apellido
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    #Definimos un método donde se van a pedir los valores del nombre y apellido que van a definir los atributos del objeto
    def leer(self):
        self.nombre = input("Nombre del autor: ")
        self.apellido = input("Apellido del autor: ")
    
    #Definimos un método para mostrar al autor
    def mostrar(self):
        print(f"Autor: {self}")


#Creamos la clase Libro
class Libro():
    def __init__(self):
        self.titulo = ""
        self.autor = Persona("", "")
        self.isbn = ""
        self.paginas = 0
        self.edicion = ""
        self.editorial = ""
        self.lugar_ciudad = ""
        self.lugar_pais = ""
        self.fecha_edicion = ""

    #Definimos los métodos getters
    def get_titulo(self):
        return self.titulo
    
    def get_autor(self):
        return self.autor
    
    def get_isbn(self):
        return self.isbn
    
    def get_paginas(self):
        return self.paginas
    
    def get_edicion(self):
        return self.edicion
    
    def get_editorial(self):
        return self.editorial
    
    def get_lugar(self):
        return f"{self.lugar_ciudad}, {self.lugar_pais}"
    
    def get_fecha(self):
        return self.fecha_edicion
    
    #Definimos los métodos setters
    def set_titulo(self, titulo):
        self.titulo = titulo;
        
    def set_autor(self, autor):
        self.autor = autor;
        
    def set_isbn(self, isbn):
        self.isbn = isbn;
        
    def set_paginas(self, paginas):
        self.paginas = paginas;
        
    def set_edicion(self, edicion):
        self.edicion = edicion;
        
    def set_editorial(self, editorial):
        self.editorial = editorial;
        
    def set_lugar(self, ciudad, pais):
        self.lugar_ciudad = ciudad;
        self.lugar_pais = pais;
        
    def set_fecha(self, fecha):
        self.fecha_edicion = fecha;
    
    #Definimos un método para leer la información
    def leer(self):
        self.titulo = input("Título del libro: ")
        print("Ingrese los datos del autor:")
        self.autor.leer()
        self.isbn = input("ISBN: ")
        self.paginas = int(input("Número de páginas: "))
        self.edicion = input("Edición: ")
        self.editorial = input("Editorial: ")
        self.lugar_ciudad = input("Ciudad: ")
        self.lugar_pais = input("Pais: ")
        self.fecha_edicion = input("Fecha de edición: ")
    
    #Definimos un método para mostrar toda la información
    def mostrar(self):
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"{self.lugar_ciudad}, {self.lugar_pais}")
        print(f"{self.fecha_edicion}")
        print(f"{self.paginas} páginas")
        
libro = Libro()
libro.leer()
libro.mostrar()