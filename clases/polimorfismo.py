# Definición de la interfaz
class Forma:
    def area(self):
        pass

# Clase que implementa la interfaz Forma para un círculo
class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        # Fórmula del área de un círculo: π * radio^2
        return 3.14 * self.radio ** 2

# Clase que implementa la interfaz Forma para un cuadrado
class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        # Fórmula del área de un cuadrado: lado^2
        return self.lado ** 2

# Función que utiliza polimorfismo para calcular el área de cualquier forma que implemente la interfaz Forma
def calcular_area(forma):
    return forma.area()

# Crear instancias de las clases
mi_circulo = Circulo(5)
mi_cuadrado = Cuadrado(4)

# Calcular y mostrar el área utilizando la función calcular_area con diferentes formas
print(f"Área del círculo: {calcular_area(mi_circulo)}")
print(f"Área del cuadrado: {calcular_area(mi_cuadrado)}")
