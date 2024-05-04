class FOIL:
    def __init__(self):
        self.antecedentes = []

    def aprender(self, ejemplos_positivos, ejemplos_negativos):
        for ejemplo in ejemplos_positivos:
            antecedente = {}
            for atributo, valor in ejemplo.items():
                if valor == 1:  # Si el valor es 1 en el ejemplo positivo, se incluye en el antecedente
                    antecedente[atributo] = valor
            self.antecedentes.append(antecedente)

        # Generar regla con FOIL
        for ejemplo in ejemplos_negativos:
            for atributo, valor in ejemplo.items():
                if valor == 1:  # Si el valor es 1 en el ejemplo negativo, se intenta refinar el antecedente
                    self.refinar_antecedentes(atributo)

    def refinar_antecedentes(self, atributo):
        nuevos_antecedentes = []
        for antecedente in self.antecedentes:
            if atributo not in antecedente:  # Si el atributo no está en el antecedente actual
                nuevo_antecedente = antecedente.copy()
                nuevo_antecedente[atributo] = 1  # Se agrega el atributo al antecedente
                nuevos_antecedentes.append(nuevo_antecedente)
        self.antecedentes.extend(nuevos_antecedentes)  # Se añaden los nuevos antecedentes a la lista

# Ejemplo de uso
foil = FOIL()

# Ejemplos de entrenamiento positivos y negativos (ejemplo ficticio)
ejemplos_positivos = [
    {"outlook": 1, "temperature": 1, "humidity": 0},
    {"outlook": 0, "temperature": 1, "humidity": 1}
]
ejemplos_negativos = [
    {"outlook": 1, "temperature": 0, "humidity": 0},
    {"outlook": 0, "temperature": 0, "humidity": 1}
]

foil.aprender(ejemplos_positivos, ejemplos_negativos)
print("Antecedentes aprendidos con FOIL:", foil.antecedentes)
