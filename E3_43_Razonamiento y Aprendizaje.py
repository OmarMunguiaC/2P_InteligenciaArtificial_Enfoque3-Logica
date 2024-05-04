class Razonamiento:
    def __init__(self, tipo):
        self.tipo = tipo

    def resolver(self, problema):
        if self.tipo == "deductivo":
            print("Realizando razonamiento deductivo...")
            # Lógica para resolver problemas mediante razonamiento deductivo
        elif self.tipo == "inductivo":
            print("Realizando razonamiento inductivo...")
            # Lógica para resolver problemas mediante razonamiento inductivo
        elif self.tipo == "abductivo":
            print("Realizando razonamiento abductivo...")
            # Lógica para resolver problemas mediante razonamiento abductivo
        else:
            print("Tipo de razonamiento no válido.")

class Aprendizaje:
    def __init__(self, tipo):
        self.tipo = tipo

    def aprender(self, datos):
        if self.tipo == "supervisado":
            print("Realizando aprendizaje supervisado...")
            # Lógica para realizar aprendizaje supervisado con los datos proporcionados
        elif self.tipo == "no supervisado":
            print("Realizando aprendizaje no supervisado...")
            # Lógica para realizar aprendizaje no supervisado con los datos proporcionados
        elif self.tipo == "reforzamiento":
            print("Realizando aprendizaje por reforzamiento...")
            # Lógica para realizar aprendizaje por reforzamiento con los datos proporcionados
        else:
            print("Tipo de aprendizaje no válido.")

razonamiento_deductivo = Razonamiento("deductivo")
razonamiento_deductivo.resolver("Problema de lógica")

aprendizaje_supervisado = Aprendizaje("supervisado")
aprendizaje_supervisado.aprender("Datos etiquetados")
