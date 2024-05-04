import heapq
import time

class Agente:
    def __init__(self, nombre, acciones):
        self.nombre = nombre
        self.acciones = acciones

class Accion:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion

class PlanificadorContinuoMultiagente:
    def __init__(self, agentes):
        self.agentes = agentes

    def ejecutar_plan(self):
        heap_acciones = []

        for agente in self.agentes:
            for accion in agente.acciones:
                heapq.heappush(heap_acciones, (time.time(), accion, agente))

        while heap_acciones:
            tiempo_inicio, accion, agente = heapq.heappop(heap_acciones)
            print(f"Agente {agente.nombre} comienza la acción: {accion.nombre} a las {tiempo_inicio}")
            time.sleep(accion.duracion)  # Simula la duración de la acción
            tiempo_fin = time.time()
            print(f"Agente {agente.nombre} completa la acción: {accion.nombre} a las {tiempo_fin}")

            # Actualizar el tiempo de inicio para replanificar
            tiempo_inicio = tiempo_fin

            # Replanificar
            heapq.heappush(heap_acciones, (tiempo_inicio, accion, agente))

# Definimos las acciones de cada agente
acciones_agente_1 = [Accion("Ir a la tienda", 3), Accion("Comprar leche", 2), Accion("Volver a casa", 3)]
acciones_agente_2 = [Accion("Ir a la tienda", 2), Accion("Comprar pan", 1), Accion("Volver a casa", 2)]

# Creamos instancias de agentes con sus acciones
agente_1 = Agente("1", acciones_agente_1)
agente_2 = Agente("2", acciones_agente_2)

# Creamos una instancia de PlanificadorContinuoMultiagente y ejecutamos el plan
planificador = PlanificadorContinuoMultiagente([agente_1, agente_2])
planificador.ejecutar_plan()
