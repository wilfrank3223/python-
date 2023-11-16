# Definición de la clase Persona
class Persona:
    # Constructor de la clase, se llama automáticamente al crear una nueva instancia
    def __init__(self, nombre, edad):
        # Atributo "nombre" de la instancia
        self.nombre = nombre
        # Atributo "edad" de la instancia
        self.edad = edad

    # Método para imprimir un saludo con el nombre y la edad de la persona
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

    # Método para incrementar la edad de la persona y mostrar un mensaje de cumpleaños
    def cumplir_anios(self):
        # Incrementar la edad en 1
        self.edad += 1
        # Mostrar un mensaje de cumpleaños con la nueva edad
        print(f"Feliz cumpleaños, ahora tengo {self.edad} años.")

# Crear una nueva instancia de la clase Persona con nombre "Juan" y edad 25
persona1 = Persona("Juan", 25)

# Acceder al atributo "nombre" de la instancia y mostrarlo
print(f"Nombre: {persona1.nombre}")

# Acceder al atributo "edad" de la instancia y mostrarlo
print(f"Edad: {persona1.edad}")

# Llamar al método "saludar" de la instancia, que imprime un saludo
persona1.saludar()

# Llamar al método "cumplir_anios" de la instancia, que incrementa la edad y muestra un mensaje de cumpleaños
persona1.cumplir_anios()
