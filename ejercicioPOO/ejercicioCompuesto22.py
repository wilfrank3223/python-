import datetime

class Equipo:
    def __init__(self, id, cargador, mouse, estado, ambiente):
        self.id = id
        self.cargador = cargador
        self.mouse = mouse
        self.estado = estado
        self.ambiente = ambiente

class Novedad:
    def __init__(self, fecha, descripcion, equipo):
        self.fecha = fecha
        self.descripcion = descripcion
        self.equipo = equipo

equipos = []
novedades = []

def agregar_equipo():
    id = input("Ingrese el ID del equipo: ")
    cargador = input("Ingrese el estado del cargador: ")
    mouse = input("Ingrese el estado del mouse: ")
    estado = input("Ingrese el estado actual del equipo: ")
    ambiente = input("Ingrese el ambiente del equipo: ")

    equipo = Equipo(id, cargador, mouse, estado, ambiente)
    equipos.append(equipo)

def editar_equipo():
    id = input("Ingrese el ID del equipo a editar: ")
    equipo = next((e for e in equipos if e.id == id), None)

    if equipo:
        print("Equipo encontrado. A continuación, puede editar la información:")
        cargador = input(f"Nuevo estado del cargador ({equipo.cargador}): ")
        mouse = input(f"Nuevo estado del mouse ({equipo.mouse}): ")
        estado = input(f"Nuevo estado actual del equipo ({equipo.estado}): ")
        ambiente = input(f"Nuevo ambiente del equipo ({equipo.ambiente}): ")

        equipo.cargador = cargador if cargador else equipo.cargador
        equipo.mouse = mouse if mouse else equipo.mouse
        equipo.estado = estado if estado else equipo.estado
        equipo.ambiente = ambiente if ambiente else equipo.ambiente

        print("Información del equipo editada con éxito.")
    else:
        print("No se encontró el equipo con el ID especificado.")

def eliminar_equipo():
    id = input("Ingrese el ID del equipo a eliminar: ")
    equipo = next((e for e in equipos if e.id == id), None)

    if equipo:
        equipos.remove(equipo)
        print("Equipo eliminado con éxito.")
    else:
        print("No se encontró el equipo con el ID especificado.")

def agregar_novedad():
    fecha = input("Ingrese la fecha de la novedad: ")
    descripcion = input("Ingrese la descripción de la novedad: ")
    equipo_id = input("Ingrese el ID del equipo relacionado: ")

    equipo = next((e for e in equipos if e.id == equipo_id), None)
    if equipo:
        novedad = Novedad(fecha, descripcion, equipo)
        novedades.append(novedad)
    else:
        print("Equipo no encontrado. No se pudo agregar la novedad.")

def mostrar_equipos_con_novedades():
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

def buscar_equipo():
    id = input("Ingrese el ID del equipo a buscar: ")
    equipo = next((e for e in equipos if e.id == id), None)

    if equipo:
        print("Información del equipo:")
        print("ID:", equipo.id)
        print("Cargador:", equipo.cargador)
        print("Mouse:", equipo.mouse)
        print("Estado actual:", equipo.estado)
        print("Ambiente:", equipo.ambiente)
    else:
        print("No se encontró el equipo con el ID especificado.")

# Ejemplo de uso
while True:
    print("\nOpciones:")
    print("1. Agregar equipo")
    print("2. Editar equipo")
    print("3. Eliminar equipo")
    print("4. Agregar novedad")
    print("5. Mostrar equipos con novedades")
    print("6. Buscar equipo")
    print("7. Salir")

    opcion = input("Seleccione una opción (1/2/3/4/5/6/7): ")

    if opcion == "1":
        agregar_equipo()
    elif opcion == "2":
        editar_equipo()
    elif opcion == "3":
        eliminar_equipo()
    elif opcion == "4":
        agregar_novedad()
    elif opcion == "5":
        mostrar_equipos_con_novedades()
    elif opcion == "6":
        buscar_equipo()
    elif opcion == "7":
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")
