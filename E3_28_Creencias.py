class Evento:
    def __init__(self, nombre, descripcion):
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return f"{self.nombre}: {self.descripcion}"

class Creencia:
    def __init__(self, sujeto, objeto, evento):
        self.sujeto = sujeto
        self.objeto = objeto
        self.evento = evento

    def __str__(self):
        return f"{self.sujeto} cree que {self.objeto} {self.evento}"

# Creamos algunos eventos
evento1 = Evento("Conferencia", "Conferencia sobre inteligencia artificial")
evento2 = Evento("Reunión", "Reunión de equipo")

# Creamos creencias sobre los eventos
creencia1 = Creencia("Juan", "evento1", "será interesante")
creencia2 = Creencia("María", "evento2", "será productiva")

# Mostramos las creencias
print(creencia1)
print(creencia2)
