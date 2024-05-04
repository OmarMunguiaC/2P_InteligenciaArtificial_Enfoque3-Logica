from pysat.solvers import Glucose3

class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre
        self.precondiciones = precondiciones
        self.efectos = efectos

class SATPLAN:
    def __init__(self, acciones, estados_iniciales, estados_meta):
        self.acciones = acciones
        self.estados_iniciales = estados_iniciales
        self.estados_meta = estados_meta
        self.solver = Glucose3()

    def codificar_estados(self, k):
        proposiciones = {}

        for i, estado in enumerate(self.estados_iniciales):
            proposiciones[(0, i, estado)] = i + 1

        for j in range(1, k + 1):
            for i in range(len(self.estados_iniciales)):
                proposiciones[(j, i, self.estados_iniciales[i])] = len(self.estados_iniciales) + i + 1 + (j - 1) * len(self.estados_iniciales)

        return proposiciones

    def codificar_acciones(self, k):
        proposiciones = {}

        for j in range(1, k + 1):
            for i, accion in enumerate(self.acciones):
                proposiciones[(j, i)] = len(self.acciones) * len(self.estados_iniciales) + (j - 1) * len(self.acciones) + i + 1

        return proposiciones

    def agregar_clausulas_iniciales(self, k, proposiciones):
        for i, estado in enumerate(self.estados_iniciales):
            self.solver.add_clause([proposiciones[(0, i, estado)]])

    def agregar_clausulas_meta(self, k, proposiciones):
        for i, estado in enumerate(self.estados_meta):
            self.solver.add_clause([proposiciones[(k, i, estado)]])

    def agregar_clausulas_intermedias(self, k, proposiciones, acciones):
        for j in range(1, k + 1):
            for i, accion in enumerate(acciones):
                precondiciones = [proposiciones[(j - 1, x, p)] for x, p in enumerate(accion.precondiciones)]
                efectos = [proposiciones[(j, x, p)] for x, p in enumerate(accion.efectos)]
                for p in precondiciones:
                    efectos.append(-p)
                self.solver.add_clause(efectos)

    def planificar(self, max_k):
        proposiciones = self.codificar_estados(max_k)
        proposiciones.update(self.codificar_acciones(max_k))

        for k in range(max_k + 1):
            self.agregar_clausulas_iniciales(k, proposiciones)
            self.agregar_clausulas_meta(k, proposiciones)
            self.agregar_clausulas_intermedias(k, proposiciones, self.acciones)

            if self.solver.solve():
                plan = self.recuperar_plan(k, proposiciones)
                return plan

        return None

    def recuperar_plan(self, k, proposiciones):
        plan = []

        for j in range(1, k + 1):
            for i, accion in enumerate(self.acciones):
                if self.solver.solve(assumptions=[proposiciones[(j, i)]]):
                    plan.append(accion.nombre)
                    break

        return plan

# Definimos acciones
accion_ir_tienda = Accion("Ir a la tienda", [], ["En la tienda"])
accion_comprar = Accion("Comprar leche", ["En la tienda"], ["Tener leche"])
accion_volver_casa = Accion("Volver a casa", ["En la tienda"], ["En casa"])

# Definimos estados iniciales y metas
estados_iniciales = ["En casa"]
estados_meta = {"Tener leche"}

# Creamos una instancia de SATPLAN y planificamos
satplan = SATPLAN([accion_ir_tienda, accion_comprar, accion_volver_casa], estados_iniciales, estados_meta)
plan = satplan.planificar(max_k=10)

# Mostramos el plan
if plan:
    print("Plan encontrado:")
    for accion in plan:
        print(accion)
else:
    print("No se pudo encontrar un plan.")
