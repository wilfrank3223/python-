import datetime  # Importar la biblioteca de fecha y hora necesaria.

# Definir una clase para almacenar la información de un equipo
class Equipo:
    def __init__(self, id, cargador, mouse, estado, ambiente):
        self.id = id  # ID del equipo
        self.cargador = cargador  # Estado del cargador
        self.mouse = mouse  # Estado del mouse
        self.estado = estado  # Estado actual del equipo
        self.ambiente = ambiente  # Nuevo atributo: Ambiente del equipo

# Definir una clase para almacenar la información de una novedad
class Novedad:
    def __init__(self, fecha, descripcion, equipo):
        self.fecha = fecha  # Fecha de la novedad
        self.descripcion = descripcion  # Descripción de la novedad
        self.equipo = equipo  # Equipo relacionado con la novedad

# Listas para almacenar equipos y novedades
equipos = []  # Lista para almacenar objetos de la clase Equipo
novedades = []  # Lista para almacenar objetos de la clase Novedad

# Definir una función para agregar un equipo
def agregar_equipo():
    id = input("Ingrese el ID del equipo: ")  # Solicitar al usuario el ID del equipo
    cargador = input("Ingrese el estado del cargador: ")  # Solicitar el estado del cargador

# Definir una función para agregar una novedad
def agregar_novedad():
    fecha = input("Ingrese la fecha de la novedad: ")  # Solicitar la fecha de la novedad
    descripcion = input("Ingrese la descripción de la novedad: ")  # Solicitar la descripción de la novedad
    equipo_id = input("Ingrese el ID del equipo relacionado: ")  # Solicitar el ID del equipo relacionado

    # Verificar si el equipo existe
    equipo = next((e for e in equipos if e.id == equipo_id), None)  # Buscar el equipo en la lista de equipos
    if equipo:
        novedad = Novedad(fecha, descripcion, equipo)  # Crear un objeto de la clase Novedad
        novedades.append(novedad)  # Agregar la novedad a la lista de novedades
    else:
        print("Equipo no encontrado. No se pudo agregar la novedad.")

# Definir una función para buscar un equipo
def buscar_equipo():
    id = input("Ingrese el ID del equipo a buscar: ")  # Solicitar al usuario el ID del equipo a buscar
    equipo = next((e for e in equipos if e.id == id), None)  # Buscar el equipo en la lista de equipos

    if equipo:
        print("Información del equipo:")  # Mostrar la información del equipo
        print("ID:", equipo.id)  # Mostrar el ID del equipo
        print("Cargador:", equipo.cargador)  # Mostrar el estado del cargador del equipo
        print("Mouse:", equipo.mouse)  # Mostrar el estado del mouse del equipo
        print("Estado actual:", equipo.estado)  # Mostrar el estado actual del equipo
    else:
        print("No se encontro informacion del equipo ")
