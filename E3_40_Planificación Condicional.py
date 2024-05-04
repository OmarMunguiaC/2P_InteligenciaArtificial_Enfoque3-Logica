class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre
        self.precondiciones = precondiciones
        self.efectos = efectos

class PlanificadorCondicional:
    def __init__(self, acciones, estado_inicial, estado_meta):
        self.acciones = acciones
        self.estado_inicial = estado_inicial
        self.estado_meta = estado_meta

    def planificar(self):
        plan = []
        estado_actual = self.estado_inicial

        while not self.satisface_estado(estado_actual, self.estado_meta):
            accion_aplicable = self.obtener_accion_aplicable(estado_actual)

            if accion_aplicable is None:
                return None  # No se puede planificar

            plan.append(accion_aplicable.nombre)
            estado_actual = self.aplicar_efectos(accion_aplicable, estado_actual)

        return plan

    def satisface_estado(self, estado, estado_meta):
        return all(prop in estado for prop in estado_meta)

    def obtener_accion_aplicable(self, estado):
        for accion in self.acciones:
            if all(precondicion in estado for precondicion in accion.precondiciones):
                return accion
        return None

    def aplicar_efectos(self, accion, estado):
        nuevo_estado = set(estado)
        nuevo_estado.difference_update(accion.precondiciones)
        nuevo_estado.update(accion.efectos)
        return nuevo_estado

# Definimos acciones
accion_ir_tienda = Accion("Ir a la tienda", {"en_casa"}, {"en_tienda"})
accion_comprar = Accion("Comprar leche", {"en_tienda"}, {"tener_leche"})
accion_volver_casa = Accion("Volver a casa", {"en_tienda"}, {"en_casa"})

# Definimos estados inicial y meta
estado_inicial = {"en_casa"}
estado_meta = {"tener_leche"}

# Creamos el planificador y planificamos
planificador = PlanificadorCondicional([accion_ir_tienda, accion_comprar, accion_volver_casa], estado_inicial, estado_meta)
plan = planificador.planificar()

# Mostramos el plan
if plan:
    print("Plan encontrado:")
    for accion in plan:
        print(accion)
else:
    print("No se pudo encontrar un plan.")
