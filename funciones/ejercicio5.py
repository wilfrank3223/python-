# Definir una función llamada 'compra' que toma tres parámetros: marca, cantidad y valor.
def compra(marca, cantidad, valor):
    # Devolver un diccionario con las claves 'marca', 'cantidad' y 'valor'.
    # El valor de 'valor' en el diccionario es el resultado de multiplicar 'valor' por 'cantidad'.
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor*cantidad
    )

# Imprimir lo comprado utilizando la función 'compra' con argumentos específicos.
# Se utilizan nombres de parámetros para mejorar la legibilidad.
print(f'Lo comprado fue: {compra(marca="AMD", cantidad=3, valor=2500000)}')
