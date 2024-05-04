class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre
        self.precondiciones = precondiciones
        self.efectos = efectos

class Estado:
    def __init__(self, nombre, proposiciones):
        self.nombre = nombre
        self.proposiciones = proposiciones

class Planificador:
    def __init__(self, acciones, estado_inicial, estado_meta):
        self.acciones = acciones
        self.estado_inicial = estado_inicial
        self.estado_meta = estado_meta

    def planificar_strips(self):
        plan = []
        estado_actual = self.estado_inicial

        while estado_actual != self.estado_meta:
            accion_aplicable = None

            for accion in self.acciones:
                if all(prop in estado_actual.proposiciones for prop in accion.precondiciones):
                    accion_aplicable = accion
                    break
            
            if accion_aplicable is None:
                return None  # No se puede planificar

            plan.append(accion_aplicable)
            estado_actual = Estado("Nuevo estado", estado_actual.proposiciones + accion_aplicable.efectos)

        return plan

    def planificar_adl(self):
        # Implementa la planificación ADL aquí
        pass

# Definimos acciones en ADL y STRIPS
accion_ir_tienda_adl = Accion("Ir a la tienda", ["en_casa"], ["en_tienda"])
accion_comprar_adl = Accion("Comprar leche", ["en_tienda", "tener_dinero"], ["tener_leche", "no_tener_dinero"])
accion_volver_casa_adl = Accion("Volver a casa", ["en_tienda"], ["en_casa"])

accion_ir_tienda_strips = Accion("Ir a la tienda", ["en_casa"], ["en_tienda"])
accion_comprar_strips = Accion("Comprar leche", ["en_tienda"], ["tener_leche"])
accion_volver_casa_strips = Accion("Volver a casa", ["en_tienda"], ["en_casa"])

# Definimos estados inicial y meta
estado_inicial = Estado("Estado inicial", ["en_casa"])
estado_meta = Estado("Estado meta", ["en_casa", "tener_leche"])

# Creamos el planificador y planificamos utilizando STRIPS y ADL
planificador1 = Planificador([accion_ir_tienda_adl, accion_comprar_adl, accion_volver_casa_adl], estado_inicial, estado_meta)
plan_strips = planificador1.planificar_strips()

planificador2 = Planificador([accion_ir_tienda_strips, accion_comprar_strips, accion_volver_casa_strips], estado_inicial, estado_meta)
plan_adl = planificador2.planificar_adl()

# Mostramos el plan obtenido con STRIPS
if plan_strips:
    print("Plan encontrado con STRIPS:")
    for accion in plan_strips:
        print(accion.nombre)
else:
    print("No se pudo encontrar un plan con STRIPS.")

# Mostrar el plan obtenido con ADL
if plan_adl:
    print("Plan encontrado con ADL:")
    for accion in plan_adl:
        print(accion.nombre)
else:
    print("No se pudo encontrar un plan con ADL.")
