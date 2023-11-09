# Definir una función llamada 'listalimpia' que toma dos parámetros: arg y result (con valor predeterminado None).
def listalimpia(arg, result=None):
    # Verificar si result es None (primera llamada a la función).
    if result is None:
        # Si result es None, inicializarlo como una lista vacía.
        result = []
    
    # Agregar el valor de 'arg' a la lista 'result'.
    result.append(arg)
    # Imprimir la lista 'result'.
    print(result)

# Llamar a la función 'listalimpia' con el argumento 'a'.
listalimpia("a")

# Llamar a la función 'listalimpia' con el argumento 'b'.
listalimpia("b")
