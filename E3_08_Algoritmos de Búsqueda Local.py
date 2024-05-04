import random

def funcion_objetivo(x):
    """
    Define la función objetivo para la que se busca el máximo local.
    En este ejemplo, se utiliza la función f(x) = -x^2 + 5x - 6.
    """
    return -(x ** 2) + 5 * x - 6

def hill_climbing(max_iter, paso, rango_inicio, rango_fin):
    """
    Implementa el algoritmo de ascenso de colinas (hill climbing).
    """
    # Inicializa el valor actual con un valor aleatorio en el rango especificado
    valor_actual = random.uniform(rango_inicio, rango_fin)
    for _ in range(max_iter):
        # Genera un nuevo valor sumando o restando el paso al valor actual
        nuevo_valor = valor_actual + random.uniform(-paso, paso)
        # Evalúa si el nuevo valor es mejor que el valor actual
        if funcion_objetivo(nuevo_valor) > funcion_objetivo(valor_actual):
            valor_actual = nuevo_valor
    return valor_actual

# Parámetros del algoritmo
max_iter = 1000  # Número máximo de iteraciones
paso = 0.1       # Tamaño del paso para generar nuevos valores
rango_inicio = 0 # Límite inferior del rango de búsqueda
rango_fin = 5    # Límite superior del rango de búsqueda

# Ejecución del algoritmo de búsqueda local
maximo_local = hill_climbing(max_iter, paso, rango_inicio, rango_fin)
print("Máximo local encontrado:", maximo_local)
print("Valor de la función objetivo en el máximo local:", funcion_objetivo(maximo_local))
