# Crear un diccionario vacío llamado 'datos'.
datos = dict()
# Alternativamente, se puede crear un diccionario vacío utilizando la sintaxis de llaves.
datos = {}

# Inicializar el diccionario 'datos' con algunas claves y valores.
datos = {'nombre': 'wilfrank', 'edad': 18}

# Imprimir el valor asociado con la clave 'nombre' en el diccionario 'datos'.
print(datos['nombre'])

# Utilizar el método get() para obtener el valor asociado con la clave 'nombre1' en el diccionario 'datos'.
# Si la clave no existe, imprimir el mensaje 'no se encuentra el elemento'.
print(datos.get('nombre1', 'no se encuentra el elemento'))
