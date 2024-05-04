class InduccionGramatical:
    def __init__(self):
        self.gramatica = []

    def aprender_gramatica(self, ejemplos):
        for ejemplo in ejemplos:
            self.gramatica.append(self.inferir_regla(ejemplo))

    def inferir_regla(self, ejemplo):
        regla = ""
        for palabra in ejemplo.split():
            if palabra.isalpha():
                regla += "X"
            else:
                regla += palabra
            regla += " "
        return regla.strip()

    def generar_ejemplo(self, regla):
        ejemplo = ""
        for simbolo in regla.split():
            if simbolo == "X":
                ejemplo += "palabra "
            else:
                ejemplo += simbolo + " "
        return ejemplo.strip()

# Ejemplo de uso
induccion = InduccionGramatical()
ejemplos = ["el gato come", "la casa es grande", "el perro ladra"]
induccion.aprender_gramatica(ejemplos)
print("Gramática aprendida:")
for regla in induccion.gramatica:
    print(regla)

print("\nGenerar ejemplo con la primera regla:")
ejemplo_generado = induccion.generar_ejemplo(induccion.gramatica[0])
print(ejemplo_generado)
