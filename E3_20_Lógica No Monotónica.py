class LógicaNoMonotónica:
    def __init__(self):
        self.hechos = set()
        self.reglas = []

    def agregar_hecho(self, hecho):
        """
        Agrega un hecho al conjunto de hechos.
        """
        self.hechos.add(hecho)

    def agregar_regla(self, antecedentes, consecuente):
        """
        Agrega una regla a la base de conocimiento.
        """
        self.reglas.append((antecedentes, consecuente))

    def inferir_consecuente(self):
        """
        Realiza inferencia para obtener el consecuente de las reglas.
        """
        for antecedentes, consecuente in self.reglas:
            if all(hecho in self.hechos for hecho in antecedentes):
                return consecuente
        return None

# Crear una instancia de lógica no monotónica
logica = LógicaNoMonotónica()

# Agregar hechos y reglas
logica.agregar_hecho('p')
logica.agregar_regla(['p'], 'q')

# Inferir consecuente
consecuente = logica.inferir_consecuente()
print("Consecuente inferido:", consecuente)
