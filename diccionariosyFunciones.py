import datetime  # Importar la biblioteca de fecha y hora necesaria.

# Definir una clase para almacenar la información de un equipo
class Equipo:
    def __init__(self, id, cargador, mouse, estado):
        self.id = id  # ID del equipo
        self.cargador = cargador  # Estado del cargador
        self.mouse = mouse  # Estado del mouse
        self.estado = estado  # Estado actual del equipo
        self.hambiente = hambiente#estado actual del equipo

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
    mouse = input("Ingrese el estado del mouse: ")  # Solicitar el estado del mouse
    estado = input("Ingrese el estado actual del equipo: ")  # Solicitar el estado actual del equipo
    hambiente = input("ingrese el hambiente:")#solicite el hambiente

    equipo = Equipo(id, cargador, mouse, estado,hambiente)  # Crear un objeto de la clase Equipo
    equipos.append(equipo)  # Agregar el equipo a la lista de equipos

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
        print("hambiente:", equipo.hambiente) #mostrar el hambiente actual del equipo
    else:
        print("No se encontró el equipo con el ID especificado.")  # Mostrar un mensaje si el equipo no se encuentra

# Definir una función para mostrar un reporte de equipos con novedades
def reporteEquiposConNovedades():
    equiposConNovedades = []  # Crear una lista para almacenar los equipos con novedades

    for novedad in novedades:  # Recorrer la lista de novedades
        equiposConNovedades.append(novedad.equipo)  # Agregar el equipo relacionado a la lista de equipos con novedades

    if len(equiposConNovedades) == 0:  # Verificar si no hay equipos con novedades
        print("No hay equipos con novedades.")  # Mostrar un mensaje si no hay equipos con novedades
    else:
        print("Equipos con novedades:")  # Mostrar un mensaje si hay equipos con novedades
        for equipo in equiposConNovedades:  # Recorrer la lista de equipos con novedades
            print("ID:", equipo.id)  # Mostrar el ID del equipo con novedades
            print("Cargador:", equipo.cargador)  # Mostrar el estado del cargador del equipo con novedades
            print("Mouse:", equipo.mouse)  # Mostrar el estado del mouse del equipo con novedades
            print("Estado actual:", equipo.estado)  # Mostrar el estado actual del equipo con novedades
            print("hambiente:",equipo.hambiente)

# Definir una función para modificar un equipo
def modificarEquipo():
    id = input("Ingrese el ID del equipo a modificar: ")  # Solicitar al usuario el ID del equipo a modificar
    equipo = next((e for e in equipos if e.id == id), None)  # Buscar el equipo en la lista de equipos

    if equipo:
        print("Equipo encontrado. A continuación, puede modificar la información:")  # Mostrar un mensaje si el equipo se encuentra
        cargador = input(f"Nuevo estado del cargador ({equipo.cargador}): ")  # Solicitar el nuevo estado del cargador
        mouse = input(f"Nuevo estado del mouse ({equipo.mouse}): ")  # Solicitar el nuevo estado del mouse
        estado = input(f"Nuevo estado actual del equipo ({equipo.estado}): ")  # Solicitar el nuevo estado actual del equipo
       

        equipo.cargador = cargador if cargador else equipo.cargador  # Actualizar el estado del cargador del equipo
        equipo.mouse = mouse if mouse else equipo.mouse  # Actualizar el estado del mouse del equipo
        equipo.estado = estado if estado else equipo.estado  # Actualizar el estado actual del equipo

        print("Información del equipo modificada con éxito.")  # Mostrar un mensaje de éxito después de la modificación
    else:
        print("No se encontró el equipo con el ID especificado.")  # Mostrar un mensaje si el equipo no se encuentra

# Ejemplo de uso
while True:
    print("\nOpciones:")
    print("1. Agregar equipo")
    print("2. Agregar novedad")
    print("3. Buscar equipo")
    print("4. Mostrar equipos con novedades")
    print("5. Modificar equipo")
    print("6. Salir")

    opcion = input("Seleccione una opción (1/2/3/4/5/6): ")

    if opcion == "1":
        agregar_equipo()
    elif opcion == "2":
        agregar_novedad()
    elif opcion == "3":
        buscar_equipo()
    elif opcion == "4":
        reporteEquiposConNovedades()
    elif opcion == "5":
        modificar_equipo()
    elif opcion == "6":
        
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

    
