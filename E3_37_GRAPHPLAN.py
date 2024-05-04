from collections import defaultdict

class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre
        self.precondiciones = precondiciones
        self.efectos = efectos

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.padres = []
        self.hijos = []

    def __str__(self):
        return self.nombre

class PlanificadorGraphplan:
    def __init__(self, acciones, estados_iniciales, estados_meta):
        self.acciones = acciones
        self.estados_iniciales = estados_iniciales
        self.estados_meta = estados_meta
        self.grafo_planificacion = defaultdict(list)

    def generar_grafo(self):
        # Añadir nodos para los estados iniciales
        for estado in self.estados_iniciales:
            nodo = Nodo(estado)
            self.grafo_planificacion[0].append(nodo)

        nivel = 0
        while True:
            acciones_aplicables = self.obtener_acciones_aplicables(nivel)

            if not acciones_aplicables or self.estados_meta <= set(nodo.nombre for nodo in self.grafo_planificacion[nivel]):
                break

            for accion in acciones_aplicables:
                nuevo_estado = self.aplicar_efectos(accion, nivel)
                nodo = Nodo(nuevo_estado)
                nodo.padres.extend(self.grafo_planificacion[nivel])
                self.grafo_planificacion[nivel+1].append(nodo)

            nivel += 1

    def obtener_acciones_aplicables(self, nivel):
        acciones_aplicables = []

        for accion in self.acciones:
            if all(precondicion in set(nodo.nombre for nodo in self.grafo_planificacion[nivel]) for precondicion in accion.precondiciones):
                acciones_aplicables.append(accion)

        return acciones_aplicables

    def aplicar_efectos(self, accion, nivel):
        nuevo_estado = set(nodo.nombre for nodo in self.grafo_planificacion[nivel])
        nuevo_estado.update(accion.efectos)
        return nuevo_estado

    def planificar(self):
        plan = []
        
        nivel = len(self.grafo_planificacion) - 1
        while nivel >= 0:
            if self.estados_meta <= set(nodo.nombre for nodo in self.grafo_planificacion[nivel]):
                plan.extend(self.recuperar_plan(nodo))
                break
            nivel -= 1

        return plan

    def recuperar_plan(self, nodo):
        plan = []

        while nodo.padres:
            accion = next(accion for accion in self.acciones if set(accion.efectos) == set(nodo.nombre for nodo in nodo.padres))
            plan.insert(0, accion.nombre)
            nodo = nodo.padres[0]

        return plan

# Definimos acciones
accion_ir_tienda = Accion("Ir a la tienda", [], ["En la tienda"])
accion_comprar = Accion("Comprar leche", ["En la tienda"], ["Tener leche"])
accion_volver_casa = Accion("Volver a casa", ["En la tienda"], ["En casa"])

# Definimos estados iniciales y metas
estados_iniciales = ["En casa"]
estados_meta = {"Tener leche"}

# Creamos una instancia del planificador GRAPHPLAN
planificador = PlanificadorGraphplan([accion_ir_tienda, accion_comprar, accion_volver_casa], estados_iniciales, estados_meta)

# Generamos el grafo de planificación
planificador.generar_grafo()

# Planificamos
plan = planificador.planificar()

# Mostramos el plan
if plan:
    print("Plan encontrado:")
    for accion in plan:
        print(accion)
else:
    print("No se pudo encontrar un plan.")
