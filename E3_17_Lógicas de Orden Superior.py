def aplicar_funcion_a_todos(funcion, lista):
    """
    Aplica una función dada a todos los elementos de una lista.
    """
    return [funcion(elemento) for elemento in lista]

def cuadrado(numero):
    """
    Calcula el cuadrado de un número.
    """
    return numero ** 2

def doble(numero):
    """
    Calcula el doble de un número.
    """
    return numero * 2

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Aplicar función de cuadrado a todos los números
cuadrados = aplicar_funcion_a_todos(cuadrado, numeros)
print("Cuadrados de los números:", cuadrados)

# Aplicar función de doble a todos los números
dobles = aplicar_funcion_a_todos(doble, numeros)
print("Dobles de los números:", dobles)
