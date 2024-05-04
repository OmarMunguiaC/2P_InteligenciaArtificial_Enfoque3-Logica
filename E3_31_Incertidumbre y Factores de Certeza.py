class Hecho:
    def __init__(self, nombre, certeza):
        self.nombre = nombre
        self.certeza = certeza

    def __str__(self):
        return f"{self.nombre} (Certeza: {self.certeza})"

class BaseConocimiento:
    def __init__(self):
        self.hechos = []

    def agregar_hecho(self, hecho):
        self.hechos.append(hecho)

    def mostrar_hechos(self):
        print("Hechos:")
        for hecho in self.hechos:
            print(hecho)

# Creamos una base de conocimiento
bc = BaseConocimiento()

# Agregamos algunos hechos con certeza
bc.agregar_hecho(Hecho("p", 0.8))
bc.agregar_hecho(Hecho("q", 0.6))
bc.agregar_hecho(Hecho("r", 0.9))

# Mostramos los hechos
bc.mostrar_hechos()
