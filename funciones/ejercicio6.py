# Definir una función llamada 'compra' que toma tres parámetros: marca, cantidad y valor (con un valor predeterminado de 5000).
def compra(marca, cantidad, valor=5000):
    # Devolver un diccionario con las claves 'marca', 'cantidad' y 'valor'.
    # El valor de 'valor' en el diccionario es el resultado de multiplicar 'valor' por 'cantidad'.
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor*cantidad
    )

# Imprimir lo comprado utilizando la función 'compra' con la marca "RYZEN" (la cantidad se asume como 1 y el valor predeterminado es 5000).
print(f'Lo comprado fue: {compra("RYZEN")}')
