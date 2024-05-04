class ConjuntoDifusoTriangular:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def pertenencia(self, x):
        """
        Calcula el grado de pertenencia de un valor dado al conjunto difuso.
        """
        if x <= self.a or x >= self.c:
            return 0
        elif self.a < x <= self.b:
            return (x - self.a) / (self.b - self.a)
        elif self.b < x < self.c:
            return (self.c - x) / (self.c - self.b)

# Crear un conjunto difuso triangular
conjunto_difuso = ConjuntoDifusoTriangular(2, 4, 6)

# Evaluar el grado de pertenencia para varios valores
valores = [1, 3, 5, 7, 9]
for valor in valores:
    grado = conjunto_difuso.pertenencia(valor)
    print(f"Grado de pertenencia de {valor} al conjunto difuso: {grado}")
