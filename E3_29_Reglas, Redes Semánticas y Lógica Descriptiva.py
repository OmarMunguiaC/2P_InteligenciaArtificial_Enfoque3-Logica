class Regla:
    def __init__(self, antecedente, consecuente):
        self.antecedente = antecedente
        self.consecuente = consecuente

    def __str__(self):
        return f"Si {self.antecedente}, entonces {self.consecuente}"

class Nodo:
    def __init__(self, nombre, relaciones=None):
        self.nombre = nombre
        self.relaciones = relaciones if relaciones else []

    def agregar_relacion(self, relacion):
        self.relaciones.append(relacion)

    def __str__(self):
        return self.nombre

# Creamos algunas reglas
regla1 = Regla("temperatura alta", "encender aire acondicionado")
regla2 = Regla("humedad alta", "encender deshumidificador")

# Creamos una red semántica
nodo1 = Nodo("temperatura")
nodo2 = Nodo("humedad")
nodo3 = Nodo("aire acondicionado")
nodo4 = Nodo("deshumidificador")

nodo1.agregar_relacion(nodo3)
nodo2.agregar_relacion(nodo4)

# Mostramos las reglas y la red semántica
print("Reglas:")
print(regla1)
print(regla2)

print("\nRed Semántica:")
print("Temperatura:", nodo1.relaciones)
print("Humedad:", nodo2.relaciones)
