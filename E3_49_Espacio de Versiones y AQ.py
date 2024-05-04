class VersionSpace:
    def __init__(self, conceptos_posibles):
        self.versiones = [{}]
        self.conceptos_posibles = conceptos_posibles

    def actualizar(self, instancia, etiqueta):
        versiones_actualizadas = []
        for version in self.versiones:
            if self.coincide(version, instancia, etiqueta):
                versiones_actualizadas.append(version)
        self.versiones = versiones_actualizadas

    def coincide(self, version, instancia, etiqueta):
        for i, valor in enumerate(instancia):
            if valor != '?' and (i not in version or version[i] != valor):
                return False
        return True

class AQ:
    def __init__(self, conceptos_posibles):
        self.version_space = VersionSpace(conceptos_posibles)

    def aprender(self, instancias_etiquetadas):
        for instancia, etiqueta in instancias_etiquetadas:
            self.version_space.actualizar(instancia, etiqueta)

# Ejemplo de uso
conceptos_posibles = ['Soleado', 'Lluvioso', 'Frío', 'Caliente', '?']
aq = AQ(conceptos_posibles)

# Conjunto de instancias etiquetadas (ejemplo ficticio)
instancias_etiquetadas = [
    (['Soleado', '?', 'Alta', 'Débil'], 'No'),
    (['Lluvioso', '?', 'Alta', 'Fuerte'], 'No'),
    (['Nublado', 'Frío', '?', 'Débil'], 'Sí'),
]

aq.aprender(instancias_etiquetadas)
print("Espacio de Versiones después de aprender:", aq.version_space.versiones)
