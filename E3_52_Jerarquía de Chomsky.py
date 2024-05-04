class GramaticaChomsky:
    def __init__(self, tipo):
        self.tipo = tipo

    def imprimir_explicacion(self):
        print("Jerarquía de Chomsky:")
        if self.tipo == 0:
            print("Tipo 0: Gramáticas Irrestrictas")
            print("Las gramáticas de tipo 0 no tienen restricciones y pueden generar cualquier lenguaje.")
            print("No hay restricciones en las reglas de producción.")
            print("Ejemplo: S -> AB | aB | a")
        elif self.tipo == 1:
            print("Tipo 1: Gramáticas Sensibles al Contexto")
            print("Las gramáticas de tipo 1 tienen reglas de producción donde la longitud de la parte derecha no puede ser menor que la de la parte izquierda.")
            print("Ejemplo: aAb -> aaaB")
        elif self.tipo == 2:
            print("Tipo 2: Gramáticas Libres de Contexto")
            print("Las gramáticas de tipo 2 tienen reglas de producción donde la parte izquierda es un solo símbolo no terminal y la parte derecha puede ser cualquier secuencia de símbolos terminales y no terminales.")
            print("Ejemplo: A -> BC | a")
        elif self.tipo == 3:
            print("Tipo 3: Gramáticas Regulares")
            print("Las gramáticas de tipo 3 tienen reglas de producción donde la parte izquierda es un solo símbolo no terminal y la parte derecha puede ser un solo símbolo terminal, un solo símbolo no terminal seguido de un terminal, o épsilon.")
            print("Ejemplo: A -> aB | a | ε")
        else:
            print("Tipo no válido. Debe ser un número entre 0 y 3.")

# Ejemplo de uso
tipo_gramatica = 2
gramatica = GramaticaChomsky(tipo_gramatica)
gramatica.imprimir_explicacion()
