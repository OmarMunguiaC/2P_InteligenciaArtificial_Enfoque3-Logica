class Marco:
    def __init__(self, nombre, atributos=None):
        self.nombre = nombre
        self.atributos = atributos if atributos else {}

    def agregar_atributo(self, nombre, valor):
        self.atributos[nombre] = valor

    def obtener_atributo(self, nombre):
        return self.atributos.get(nombre, None)

# Definimos marcos para acciones, situaciones y eventos
accion = Marco("Accion")
situacion = Marco("Situacion")
evento = Marco("Evento")

# Definimos atributos para cada marco
accion.agregar_atributo("realizada_por", "persona")
situacion.agregar_atributo("tiempo", "hora")
evento.agregar_atributo("lugar", "ubicacion")

# Mostramos los marcos y sus atributos
print("Marco Accion:")
print("Realizada por:", accion.obtener_atributo("realizada_por"))
print("\nMarco Situacion:")
print("Tiempo:", situacion.obtener_atributo("tiempo"))
print("\nMarco Evento:")
print("Lugar:", evento.obtener_atributo("lugar"))
