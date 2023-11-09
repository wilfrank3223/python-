# Definir una función llamada 'compra' que toma tres parámetros: marca, cantidad y valor.
def compra(marca, cantidad, valor):
    # Devolver un diccionario con las claves 'marca', 'cantidad' y 'valor'.
    # El valor de 'valor' en el diccionario es el resultado de multiplicar 'valor' por 'cantidad'.
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor*cantidad
    )

# Imprimir lo comprado utilizando la función 'compra' con argumentos ("AMD", 3, 2500000).
print(f'Lo comprado fue: {compra("AMD", 3, 2500000)}')
