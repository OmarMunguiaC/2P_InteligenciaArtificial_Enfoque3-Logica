class Mundo:
    def __init__(self, nombre, props):
        self.nombre = nombre
        self.props = props

class Agente:
    def __init__(self):
        self.mundos = {}

    def agregar_mundo(self, nombre, props):
        """
        Agrega un mundo al agente.
        """
        self.mundos[nombre] = Mundo(nombre, props)

    def evaluar_proposicion(self, mundo, proposicion):
        """
        Evalúa una proposición en un mundo dado.
        """
        return proposicion in mundo.props

# Crear un agente
agente = Agente()

# Agregar mundos al agente
agente.agregar_mundo("mundo1", {"p", "q"})
agente.agregar_mundo("mundo2", {"p", "~q"})
agente.agregar_mundo("mundo3", {"~p", "q"})
agente.agregar_mundo("mundo4", {"~p", "~q"})

# Definir una proposición modal
proposicion_modal = "posible p"

# Evaluar la proposición modal en cada mundo
for nombre_mundo, mundo in agente.mundos.items():
    evaluacion = agente.evaluar_proposicion(mundo, "p")
    print(f"En el mundo {nombre_mundo}, p es {'' if evaluacion else 'no '}verdadero")

    if proposicion_modal.startswith("posible"):
        proposicion = proposicion_modal.split()[1]
        evaluacion_prop_modal = any(agente.evaluar_proposicion(otro_mundo, proposicion) for otro_mundo in agente.mundos.values())
        print(f"La proposición modal '{proposicion_modal}' es {'verdadera' if evaluacion_prop_modal else 'falsa'} en el mundo {nombre_mundo}")

