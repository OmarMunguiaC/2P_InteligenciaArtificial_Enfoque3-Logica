class LógicaPorDefecto:
    def __init__(self):
        self.hechos = set()
        self.regla_por_defecto = []

    def agregar_hecho(self, hecho):
        """
        Agrega un hecho al conjunto de hechos.
        """
        self.hechos.add(hecho)

    def agregar_regla_por_defecto(self, antecedentes, consecuente):
        """
        Agrega una regla por defecto a la base de conocimiento.
        """
        self.regla_por_defecto.append((antecedentes, consecuente))

    def inferir_consecuente(self):
        """
        Realiza inferencia para obtener el consecuente de las reglas por defecto.
        """
        for antecedentes, consecuente in self.regla_por_defecto:
            if all(hecho in self.hechos for hecho in antecedentes):
                return consecuente
        return None

# Crear una instancia de lógica por defecto
logica = LógicaPorDefecto()

# Agregar hechos y reglas por defecto
logica.agregar_hecho('p')
logica.agregar_regla_por_defecto(['p'], 'q')

# Inferir consecuente
consecuente = logica.inferir_consecuente()
print("Consecuente inferido:", consecuente)
