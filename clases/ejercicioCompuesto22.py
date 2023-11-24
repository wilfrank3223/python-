import datetime

# Define una clase para almacenar información sobre un equipo
class Equipo:
    def __init__(self, id, cargador, mouse, estado, ambiente):
        self.id = id  # ID del equipo
        self.cargador = cargador  # Estado del cargador
        self.mouse = mouse  # Estado del mouse
        self.estado = estado  # Estado actual del equipo
        self.ambiente = ambiente  # Nuevo atributo: Ambiente del equipo

# Define una clase para almacenar información sobre una novedad
class Novedad:
    def __init__(self, fecha, descripcion, equipo):
        self.fecha = fecha  # Fecha de la novedad
        self.descripcion = descripcion  # Descripción de la novedad
        self.equipo = equipo  # Equipo relacionado con la novedad

# Listas para almacenar equipos y novedades
equipos = []  # Lista para almacenar objetos de la clase Equipo
novedades = []  # Lista para almacenar objetos de la clase Novedad

# Define una función para agregar un equipo
def agregarEquipo():
    id = input("Ingrese el ID del equipo: ")  # Solicitar al usuario el ID del equipo
    cargador = input("Ingrese el estado del cargador: ")  # Solicitar el estado del cargador
    mouse = input("Ingrese el estado del mouse: ")  # Solicitar el estado del mouse
    estado = input("Ingrese el estado actual del equipo: ")  # Solicitar el estado actual del equipo
    ambiente = input("Ingrese el ambiente del equipo: ")  # Solicitar el ambiente del equipo

    equipo = Equipo(id, cargador, mouse, estado, ambiente)  # Crear un objeto de la clase Equipo
    equipos.append(equipo)  # Agregar el equipo a la lista de equipos

# Define una función para agregar una novedad
def agregarNovedad():
    fecha = input("Ingrese la fecha de la novedad: ")  # Solicitar la fecha de la novedad
    descripcion = input("Ingrese la descripción de la novedad: ")  # Solicitar la descripción de la novedad
    equipoId = input("Ingrese el ID del equipo relacionado: ")  # Solicitar el ID del equipo relacionado

    # Verificar si el equipo existe
    equipo = next((e for e in equipos if e.id == equipoId), None)  # Buscar el equipo en la lista de equipos
    if equipo:
        novedad = Novedad(fecha, descripcion, equipo)  # Crear un objeto de la clase Novedad
        novedades.append(novedad)  # Agregar la novedad a la lista de novedades
    else:
        print("Equipo no encontrado. No se pudo agregar la novedad.")

# Define una función para buscar un equipo
def buscarEquipo():
    id = input("Ingrese el ID del equipo a buscar: ")  # Solicitar al usuario el ID del equipo a buscar
    equipo = next((e for e in equipos if e.id == id), None)  # Buscar el equipo en la lista de equipos

    if equipo:
        print("Información del equipo:")  # Mostrar la información del equipo
        print("ID:", equipo.id)  # Mostrar el ID del equipo
        print("Cargador:", equipo.cargador)  # Mostrar el estado del cargador del equipo
        print("Mouse:", equipo.mouse)  # Mostrar el estado del mouse del equipo
        print("Estado actual:", equipo.estado)  # Mostrar el estado actual del equipo
    else:
        print("No se encontró información del equipo.")

# Define una función para mostrar equipos con novedades
def mostrarEquiposConNovedades():
    equipos_con_novedades = [novedad.equipo for novedad in novedades]

    if len(equipos_con_novedades) == 0:
        print("No hay equipos con novedades.")
    else:
        print("Equipos con novedades:")
        for equipo in equipos_con_novedades:
            print("ID:", equipo.id)
            print("Cargador:", equipo.cargador)
            print("Mouse:", equipo.mouse)
            print("Estado actual:", equipo.estado)
            print("Ambiente:", equipo.ambiente)

# Ejemplo de uso
while True:
    print("\nOpciones:")
    print("1. Agregar equipo")
    print("2. Agregar novedad")
    print("3. Buscar equipo")
    print("4. Mostrar equipos con novedades")
    print("5. Salir")

    opcion = input("Seleccione una opción (1/2/3/4/5): ")

    if opcion == "1":
        agregarEquipo()
    elif opcion == "2":
        agregarNovedad()
    elif opcion == "3":
        buscarEquipo()
    elif opcion == "4":
        mostrarEquiposConNovedades()
    elif opcion == "5":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
