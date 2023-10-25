# Inicializa dos listas vacías para almacenar los nombres de los aprendices y sus edades.
aprendices = []
edades = []

# Llena las listas solicitando datos al usuario hasta que se ingrese un nombre en blanco.
while True:
    nombre = input("Nombre del aprendiz: ")
    if nombre == "":
        break
    edad = int(input("Edad del aprendiz: "))
    # Agrega el nombre a la lista de aprendices y la edad a la lista de edades.
    aprendices.append(nombre)
    edades.append(edad)

# Imprime las listas de aprendices y edades.
print("Lista de aprendices:", aprendices)
print("Lista de edades:", edades)

# Encuentra al aprendiz con la mayor edad.
mayor_edad = max(edades)
mayor_edad = edades.index(mayor_edad)
print("El aprendiz con la mayor edad es:", aprendices[mayor_edad])

# Inserta el nombre de la instructora en la posición 1 de la lista de aprendices.
instructora = input("Nombre de la instructora: ")
aprendices.insert(1, instructora)

# Cuenta cuántos aprendices tienen 18 años.
contador_18 = 0
for edad in edades:
    if edad == 18:
        contador_18 += 1
print("El número de aprendices con 18 años es:", contador_18)

# Agrega un aprendiz ficticio llamado "x" al final de la lista de aprendices.
aprendices.append("x")

# Borra el nombre de la instructora de la lista de aprendices.
aprendices.remove(instructora)

# Solicita un dato a buscar en la lista de aprendices y verifica si está presente.
dato_a_buscar = input("Dato a buscar en la lista de aprendices: ")
if dato_a_buscar in aprendices:
    print("El dato", dato_a_buscar, "se encuentra en la lista de aprendices.")
else:
    print("El dato", dato_a_buscar, "no se encuentra en la lista de aprendices.")

# Muestra los primeros 10 aprendices de la lista.
print("Los primeros 10 aprendices de la lista son:", aprendices[:10])

# Muestra los 10 últimos aprendices de la lista.
print("Los 10 últimos aprendices de la lista son:", aprendices[-10:])

# Muestra los elementos desde el 10 al 20 de la lista.
print("Los aprendices del elemento 10 al elemento 20 son:", aprendices[10:20])
