# Definición de la clase base Animal
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hacer_sonido(self):
        # Método que debe ser implementado por las subclases
        raise NotImplementedError("Subclases deben implementar este método")

# Subclase de Animal para representar a un Perro
class Perro(Animal):
    def hacer_sonido(self):
        # Implementación específica de hacer_sonido para un Perro
        return "¡Guau!"

# Subclase de Animal para representar a un Gato
class Gato(Animal):
    def hacer_sonido(self):
        # Implementación específica de hacer_sonido para un Gato
        return "¡Miau!"

# Subclase de Animal para representar a un Pajaro
class Pajaro(Animal):
    def hacer_sonido(self):
        # Implementación específica de hacer_sonido para un Pajaro
        return "¡Pío!"

# Función que utiliza polimorfismo para hacer sonar a un animal
def hacer_sonar(animal):
    # Muestra el nombre del animal y el sonido que hace
    print(f"{animal.nombre} dice: {animal.hacer_sonido()}")

# Crear instancias de las subclases
mi_perro = Perro("Buddy")
mi_gato = Gato("Whiskers")
mi_pajaro = Pajaro("Tweety")

# Llamar a la función hacer_sonar con diferentes tipos de animales
hacer_sonar(mi_perro)  # Salida: Buddy dice: ¡Guau!
hacer_sonar(mi_gato)   # Salida: Whiskers dice: ¡Miau!
hacer_sonar(mi_pajaro) # Salida: Tweety dice: ¡Pío!
