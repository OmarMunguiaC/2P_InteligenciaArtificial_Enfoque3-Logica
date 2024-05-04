class SistemaExperto:
    def __init__(self):
        self.base_conocimiento = {}
    
    def agregar_regla(self, antecedentes, consecuente):
        self.base_conocimiento[tuple(antecedentes)] = consecuente
    
    def inferir(self, hechos):
        for antecedentes, consecuente in self.base_conocimiento.items():
            if all(hecho in hechos for hecho in antecedentes):
                return consecuente
        return None

# Creamos una instancia del sistema experto
sistema_experto = SistemaExperto()

# Agregamos algunas reglas
sistema_experto.agregar_regla(["p", "q"], "r")
sistema_experto.agregar_regla(["s"], "t")

# Definimos algunos hechos iniciales
hechos = ["p", "q", "s"]

# Realizamos la inferencia
resultado = sistema_experto.inferir(hechos)

# Mostramos el resultado de la inferencia
if resultado:
    print("Conclusión inferida:", resultado)
else:
    print("No se pudo inferir ninguna conclusión.")
