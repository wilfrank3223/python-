# Definir una función llamada 'raiz' que toma un valor como parámetro y devuelve su raíz cuadrada.
def raiz(value):
    return value ** (1/2)

# Imprimir la raíz cuadrada del valor 4 utilizando la función 'raiz'.
print(f'La raíz cuadrada es: {raiz(4)}')

# Definir una función llamada 'validarsiexiste' que verifica si un objeto es verdadero o falso.
def validarsiexiste(obj):
    if obj:
        print(f"{obj} is True")  # Imprimir un mensaje si el objeto es verdadero.
    else:
        print(f"{obj} is False")  # Imprimir un mensaje si el objeto es falso.

# Llamar a la función 'validarsiexiste' con el valor 1 como argumento.
validarsiexiste(1)
