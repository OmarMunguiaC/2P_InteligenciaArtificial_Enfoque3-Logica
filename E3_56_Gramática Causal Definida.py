class DCG:
    def __init__(self):
        self.reglas = []

    def agregar_regla(self, regla):
        self.reglas.append(regla)

    def parse(self, entrada):
        for regla in self.reglas:
            resultado = regla.parse(entrada)
            if resultado:
                return resultado
        return None

class Regla:
    def __init__(self, nombre, secuencia_tokens):
        self.nombre = nombre
        self.secuencia_tokens = secuencia_tokens

    def parse(self, entrada):
        if len(self.secuencia_tokens) > len(entrada):
            return None

        for i, token in enumerate(self.secuencia_tokens):
            if entrada[i] != token:
                return None

        return (self.nombre, entrada[len(self.secuencia_tokens):])

# Crear una instancia de la Gramática Causal Definida
gramatica = DCG()

# Definir las reglas gramaticales
gramatica.agregar_regla(Regla("oracion", ["el", "gato", "come", "el", "gato"]))
gramatica.agregar_regla(Regla("oracion", ["el", "gato", "come", "la", "gato"]))
gramatica.agregar_regla(Regla("oracion", ["el", "gato", "come", "el", "ratón"]))
gramatica.agregar_regla(Regla("oracion", ["el", "gato", "come", "la", "ratón"]))
gramatica.agregar_regla(Regla("oracion", ["la", "gato", "come", "el", "gato"]))
gramatica.agregar_regla(Regla("oracion", ["la", "gato", "come", "la", "gato"]))
gramatica.agregar_regla(Regla("oracion", ["la", "gato", "come", "el", "ratón"]))
gramatica.agregar_regla(Regla("oracion", ["la", "gato", "come", "la", "ratón"]))
gramatica.agregar_regla(Regla("oracion", ["gato", "come", "el", "gato"]))
gramatica.agregar_regla(Regla("oracion", ["gato", "come", "la", "gato"]))
gramatica.agregar_regla(Regla("oracion", ["gato", "come", "el", "ratón"]))
gramatica.agregar_regla(Regla("oracion", ["gato", "come", "la", "ratón"]))
gramatica.agregar_regla(Regla("oracion", ["ratón", "come", "el", "gato"]))
gramatica.agregar_regla(Regla("oracion", ["ratón", "come", "la", "gato"]))
gramatica.agregar_regla(Regla("oracion", ["ratón", "come", "el", "ratón"]))
gramatica.agregar_regla(Regla("oracion", ["ratón", "come", "la", "ratón"]))

# Ejemplo de uso
entrada = ["el", "gato", "come", "el", "ratón"]
resultado = gramatica.parse(entrada)
if resultado:
    print("La entrada sigue la gramática:", resultado[0])
else:
    print("La entrada no sigue ninguna regla de la gramática.")
