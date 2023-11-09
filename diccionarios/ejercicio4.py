# Crear un diccionario llamado 'datos' con claves 'nombre' y 'notafinal', y sus respectivos valores.
datos = {
    'nombre': 'adriana',
    'notafinal': 4.5
}

# Crear otro diccionario llamado 'datos1' con claves de nombres y sus respectivas notas finales.
datos1 = {
    'wilfrank': 5.0,
    'marco': 5.0,
    'felipe': 4.5,
    'edgar': 2.5
}

# Iterar a través de las claves y valores del diccionario 'datos' utilizando un bucle 'for'.
for clave, valor in datos.items():
    print(clave, valor)
