class BaseConocimiento:
    def __init__(self):
        self.hechos = set()
        self.reglas = []

    def agregar_hecho(self, hecho):
        self.hechos.add(hecho)

    def agregar_regla(self, antecedentes, consecuente):
        self.reglas.append((antecedentes, consecuente))

    def inferir_consecuente(self):
        consecuentes = set()
        for antecedentes, consecuente in self.reglas:
            if all(hecho in self.hechos for hecho in antecedentes):
                consecuentes.add(consecuente)
        return consecuentes

# Creamos una base de conocimiento
bc = BaseConocimiento()

# Agregamos hechos
bc.agregar_hecho("p")
bc.agregar_hecho("q")

# Agregamos reglas
bc.agregar_regla(["p"], "r")
bc.agregar_regla(["q"], "s")

# Inferimos los consecuentes
print("Consecuentes inferidos:", bc.inferir_consecuente())

# Agregamos más información
bc.agregar_hecho("r")

# Volvemos a inferir los consecuentes
print("Consecuentes inferidos con más información:", bc.inferir_consecuente())
