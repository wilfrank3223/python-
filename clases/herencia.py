# Definición de la clase base
class Animal:
    # Constructor de la clase base que inicializa el nombre del animal
    def __init__(self, nombre):
        self.nombre = nombre

    # Método que debe ser implementado por las subclases
    def hablar(self):
        raise NotImplementedError("Subclases deben implementar este método")

# Clase que hereda de Animal
class Perro(Animal):
    # Implementación del constructor para la subclase Perro
    def __init__(self, nombre):
        # Llamar al constructor de la clase base para inicializar el nombre
        super().__init__(nombre)

    # Implementación del método hablar para la subclase Perro
    def hablar(self):
        return f"{self.nombre} dice ¡Guau!"

# Clase que hereda de Animal
class Gato(Animal):
    # Implementación del constructor para la subclase Gato
    def __init__(self, nombre):
        # Llamar al constructor de la clase base para inicializar el nombre
        super().__init__(nombre)

    # Implementación del método hablar para la subclase Gato
    def hablar(self):
        return f"{self.nombre} dice ¡Miau!"

# Crear instancias de las subclases
mi_perro = Perro("Buddy")
mi_gato = Gato("Whiskers")

# Llamar al método hablar de las subclases
print(mi_perro.hablar())  # Salida: Buddy dice ¡Guau!
print(mi_gato.hablar())   # Salida: Whiskers dice ¡Miau!
