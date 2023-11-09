# Definir una lambda llamada 'numeroPalabras' que toma un parámetro 't' y devuelve la cantidad de palabras en 't'.
numeroPalabras = lambda t: len(t.strip().split())

# Imprimir el resultado de la lambda 'numeroPalabras' con un ejemplo de texto.
print(numeroPalabras("hola, esto es una prueba con lambda"))

# Definir una lambda llamada 'suma' que toma dos parámetros 'x' e 'y' y devuelve la suma de ambos.
suma = lambda x, y: x + y
# Calcular la suma de 5 y 3 utilizando la lambda 'suma'.
resultado = suma(5, 3)
# Imprimir el resultado de la suma.
print(resultado)

# Definir una lambda llamada 'cuadrado' que toma un parámetro 'x' y devuelve el cuadrado de 'x'.
cuadrado = lambda x: x**2
# Calcular el cuadrado de 6 utilizando la lambda 'cuadrado'.
resultado_cuadrado = cuadrado(6)
# Imprimir el resultado del cuadrado.
print(resultado_cuadrado)
