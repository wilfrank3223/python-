# Crear un diccionario vacío llamado 'datos'.
datos = {}

# Inicializar el diccionario con una clave 'nombre' y un valor 'wilfrank', y una clave 'edad' y un valor 18.
datos = {'nombre': 'wilfrank', 'edad': 18}

# Eliminar la clave 'nombre' del diccionario 'datos'.
del(datos['nombre'])

# Agregar nuevas claves y valores al diccionario 'datos'.
datos.update({'ciudad': 'ibague', 'tel': 3173427208})

# Iterar a través de las claves y valores del diccionario 'datos' utilizando un bucle 'for'.
for i, j in datos.items():
    print(i, j)
