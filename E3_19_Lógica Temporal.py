class MundoTemporal:
    def __init__(self, nombre, props, tiempo):
        self.nombre = nombre
        self.props = props
        self.tiempo = tiempo

class AgenteTemporal:
    def __init__(self):
        self.mundos = []

    def agregar_mundo(self, nombre, props, tiempo):
        """
        Agrega un mundo temporal al agente.
        """
        self.mundos.append(MundoTemporal(nombre, props, tiempo))

    def evaluar_proposicion(self, tiempo, proposicion):
        """
        Evalúa una proposición en un momento de tiempo dado.
        """
        return [mundo for mundo in self.mundos if mundo.tiempo == tiempo and proposicion in mundo.props]

# Crear un agente temporal
agente_temporal = AgenteTemporal()

# Agregar mundos temporales al agente
agente_temporal.agregar_mundo("mundo1", {"p", "q"}, 1)
agente_temporal.agregar_mundo("mundo2", {"p", "~q"}, 2)
agente_temporal.agregar_mundo("mundo3", {"~p", "q"}, 3)
agente_temporal.agregar_mundo("mundo4", {"~p", "~q"}, 4)

# Definir una proposición temporal
proposicion_temporal = "en el futuro p"

# Evaluar la proposición temporal en cada momento de tiempo
for tiempo in range(1, 5):
    mundos_evaluados = agente_temporal.evaluar_proposicion(tiempo, "p")
    print(f"En el tiempo {tiempo}, p es verdadero en los mundos:")
    for mundo in mundos_evaluados:
        print(f"- {mundo.nombre}")

    if proposicion_temporal.startswith("en el futuro"):
        proposicion = proposicion_temporal.split()[2]
        mundos_futuros_evaluados = agente_temporal.evaluar_proposicion(tiempo + 1, proposicion)
        print(f"La proposición temporal '{proposicion_temporal}' es verdadera en los mundos futuros del tiempo {tiempo}:")
        for mundo in mundos_futuros_evaluados:
            print(f"- {mundo.nombre}")
