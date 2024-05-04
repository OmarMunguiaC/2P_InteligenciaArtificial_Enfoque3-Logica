from sympy import symbols, And, Or, Not, satisfiable

class SistemaInferencia:
    def __init__(self, reglas):
        self.reglas = reglas

    def encadenamiento_hacia_adelante(self, hechos):
        """
        Realiza encadenamiento hacia adelante.
        """
        nuevo_hecho = True
        while nuevo_hecho:
            nuevo_hecho = False
            for regla, conclusion in self.reglas.items():
                if satisfiable(And(*regla), hechos):
                    if conclusion not in hechos:
                        hechos.add(conclusion)
                        nuevo_hecho = True
        return hechos

    def encadenamiento_hacia_atras(self, meta, hechos=set()):
        """
        Realiza encadenamiento hacia atrás.
        """
        if meta in hechos:
            return True
        for regla, conclusion in self.reglas.items():
            if conclusion == meta:
                if all(self.encadenamiento_hacia_atras(premisa, hechos) for premisa in regla):
                    hechos.add(meta)
                    return True
        return False

p, q, r = symbols('p q r')
reglas = {
    (p, q): r,
    (p, r): q,
    (q, r): p
}
sistema = SistemaInferencia(reglas)

# Encadenamiento hacia adelante
print("Encadenamiento hacia adelante:")
hechos = sistema.encadenamiento_hacia_adelante(set([p, q]))
print("Hechos:", hechos)

# Encadenamiento hacia atrás
print("\nEncadenamiento hacia atrás:")
meta = p
resultado = sistema.encadenamiento_hacia_atras(meta)
print(f"¿Se puede probar la meta '{meta}'?: {resultado}")
