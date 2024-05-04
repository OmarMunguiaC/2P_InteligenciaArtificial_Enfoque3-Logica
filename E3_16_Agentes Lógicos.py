from collections import deque

class SudokuAgenteLogico:
    def __init__(self, tablero):
        self.tablero = tablero

    def es_valido(self, fila, columna, valor):
        """
        Verifica si un valor dado puede ser colocado en una posición dada en el tablero.
        """
        # Verifica la fila y la columna
        for i in range(9):
            if self.tablero[fila][i] == valor or self.tablero[i][columna] == valor:
                return False
        # Verifica el cuadrante 3x3
        cuadrante_fila_inicio = (fila // 3) * 3
        cuadrante_columna_inicio = (columna // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.tablero[cuadrante_fila_inicio + i][cuadrante_columna_inicio + j] == valor:
                    return False
        return True

    def encontrar_celda_vacia(self):
        """
        Encuentra la próxima celda vacía en el tablero.
        """
        for fila in range(9):
            for columna in range(9):
                if self.tablero[fila][columna] == 0:
                    return fila, columna
        return None, None  # Si no hay celdas vacías

    def resolver(self):
        """
        Resuelve el Sudoku utilizando búsqueda primero en anchura.
        """
        fila, columna = self.encontrar_celda_vacia()
        if fila is None:
            return True  # Si no hay más celdas vacías, se ha resuelto el Sudoku
        for valor in range(1, 10):
            if self.es_valido(fila, columna, valor):
                self.tablero[fila][columna] = valor
                if self.resolver():
                    return True
                self.tablero[fila][columna] = 0  # Retrocede si la solución es inválida
        return False

    def imprimir_tablero(self):
        """
        Imprime el tablero del Sudoku.
        """
        for fila in self.tablero:
            print(" ".join(map(str, fila)))

tablero = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

agente = SudokuAgenteLogico(tablero)
print("Tablero inicial:")
agente.imprimir_tablero()

print("\nResolviendo Sudoku...")
if agente.resolver():
    print("\nSolución encontrada:")
    agente.imprimir_tablero()
else:
    print("\nNo se encontró solución para el Sudoku.")
