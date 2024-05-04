class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre
        self.precondiciones = precondiciones
        self.efectos = efectos

class PlanificadorOrdenParcial:
    def __init__(self, acciones):
        self.acciones = acciones

    def planificar(self):
        plan = []
        acciones_restantes = self.acciones[:]

        while acciones_restantes:
            accion_elegida = None

            for accion in acciones_restantes:
                if all(efecto in plan for efecto in accion.precondiciones):
                    accion_elegida = accion
                    break
            
            if accion_elegida is None:
                return None  # No se puede planificar

            plan.append(accion_elegida.nombre)
            acciones_restantes.remove(accion_elegida)

        return plan

# Definimos acciones
accion_ir_comprar = Accion("Ir a comprar", [], ["Tener comida"])
accion_preparar_comida = Accion("Preparar comida", ["Tener comida"], ["Comida lista"])
accion_cenar = Accion("Cenar", ["Comida lista"], ["Cena terminada"])

# Creamos una instancia del planificador de orden parcial
planificador = PlanificadorOrdenParcial([accion_ir_comprar, accion_preparar_comida, accion_cenar])

# Planificamos el orden parcial de las acciones
plan = planificador.planificar()

# Mostramos el plan
if plan:
    print("Plan encontrado:")
    for i, accion in enumerate(plan, 1):
        print(f"{i}. {accion}")
else:
    print("No se pudo encontrar un plan.")
