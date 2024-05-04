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

class ReglaProduccion:
    def __init__(self, antecedente, consecuente):
        self.antecedente = antecedente
        self.consecuente = consecuente

class InferenciaDifusa:
    def __init__(self):
        self.reglas = []

    def agregar_regla(self, regla):
        """
        Agrega una regla de producción a la base de conocimiento.
        """
        self.reglas.append(regla)

    def inferir_consecuente(self, entradas):
        """
        Realiza inferencia difusa para obtener el consecuente de las reglas de producción.
        """
        grados_pertenencia = []
        for regla in self.reglas:
            minimo = min(entradas[antecedente] for antecedente in regla.antecedente)
            grados_pertenencia.append(minimo)

        return max(grados_pertenencia)

# Crear conjuntos difusos para las entradas y el consecuente
entrada_1 = ConjuntoDifusoTriangular(1, 3, 5)
entrada_2 = ConjuntoDifusoTriangular(2, 4, 6)
consecuente = ConjuntoDifusoTriangular(3, 5, 7)

# Crear reglas de producción
regla_1 = ReglaProduccion(['entrada_1'], 'consecuente')
regla_2 = ReglaProduccion(['entrada_2'], 'consecuente')

# Crear instancia de inferencia difusa y agregar reglas
inferencia = InferenciaDifusa()
inferencia.agregar_regla(regla_1)
inferencia.agregar_regla(regla_2)

# Evaluar inferencia difusa para diferentes entradas
entradas = {'entrada_1': 2.5, 'entrada_2': 3.5}
resultado = inferencia.inferir_consecuente(entradas)
print("Grado de pertenencia del consecuente:", resultado)
