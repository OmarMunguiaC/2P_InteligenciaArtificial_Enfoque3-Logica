class ModeloProbabilistaRacional:
    def __init__(self):
        self.distribucion = {}

    def agregar_probabilidad(self, evento, probabilidad):
        self.distribucion[evento] = probabilidad

    def inferir_probabilidad(self, evento):
        return self.distribucion.get(evento, 0)

# Creamos una instancia del modelo probabilista racional
modelo = ModeloProbabilistaRacional()

# Agregamos algunas probabilidades
modelo.agregar_probabilidad("Lluvioso", 0.3)
modelo.agregar_probabilidad("No Lluvioso", 0.7)

# Inferimos la probabilidad de eventos
probabilidad_lluvioso = modelo.inferir_probabilidad("Lluvioso")
probabilidad_no_lluvioso = modelo.inferir_probabilidad("No Lluvioso")

# Mostramos los resultados
print("Probabilidad de que sea Lluvioso:", probabilidad_lluvioso)
print("Probabilidad de que no sea Lluvioso:", probabilidad_no_lluvioso)
