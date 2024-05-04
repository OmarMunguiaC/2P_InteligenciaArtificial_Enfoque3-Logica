def es_valido(tablero, fila, columna):
    """
    Verifica si es seguro colocar una reina en la posición (fila, columna) en el tablero.
    """
    # Verifica si hay otra reina en la misma columna
    for i in range(fila):
        if tablero[i] == columna:
            return False
        # Verifica diagonales
        if abs(tablero[i] - columna) == abs(i - fila):
            return False
    return True

def resolver_n_reinas(n):
    """
    Resuelve el problema de las N reinas utilizando backtracking.
    """
    tablero = [-1] * n  # Inicializa el tablero
    soluciones = []

    def backtrack(fila):
        """
        Función interna para realizar backtracking recursivo.
        """
        if fila == n:  # Si todas las reinas están colocadas
            soluciones.append(tablero[:])  # Se encontró una solución válida
            return

        # Intenta colocar la reina en cada columna de la fila actual
        for columna in range(n):
            if es_valido(tablero, fila, columna):
                tablero[fila] = columna  # Coloca la reina
                backtrack(fila + 1)     # Mueve a la siguiente fila

    backtrack(0)  # Comienza con la primera fila
    return soluciones

# Ejemplo de uso
n = 4
soluciones = resolver_n_reinas(n)
print(f"Se encontraron {len(soluciones)} soluciones para el problema de las {n} reinas:")
for idx, solucion in enumerate(soluciones, start=1):
    print(f"Solución {idx}: {solucion}")
