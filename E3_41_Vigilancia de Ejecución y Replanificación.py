import time

class Accion:
    def __init__(self, nombre, duracion):
        self.nombre = nombre
        self.duracion = duracion

class VigilanciaReplanificacion:
    def __init__(self, acciones, estado_actual):
        self.acciones = acciones
        self.estado_actual = estado_actual

    def ejecutar_accion(self, accion):
        print(f"Ejecutando acción: {accion.nombre}")
        time.sleep(accion.duracion)  # Simula la duración de la acción
        print(f"Acción completada: {accion.nombre}")

    def vigilar_ejecucion(self):
        for accion in self.acciones:
            if accion.nombre not in self.estado_actual:
                print(f"¡Alerta! Acción {accion.nombre} no se ha completado.")
                return False
        print("Todas las acciones se han completado.")
        return True

    def replanificar(self):
        acciones_pendientes = [accion for accion in self.acciones if accion.nombre not in self.estado_actual]
        print("Replanificando acciones pendientes...")
        print("Acciones pendientes:", [accion.nombre for accion in acciones_pendientes])

        # Aquí iría la lógica para generar un nuevo plan en base a las acciones pendientes
        # En este ejemplo, simplemente imprimimos un mensaje indicando que se ha replanificado

    def ejecutar_plan(self):
        for accion in self.acciones:
            self.ejecutar_accion(accion)
            self.estado_actual.add(accion.nombre)
            if not self.vigilar_ejecucion():
                self.replanificar()
                self.ejecutar_plan()
                break

# Definimos las acciones con sus respectivas duraciones
accion_ir_comprar = Accion("Ir a comprar", 3)
accion_comprar = Accion("Comprar leche", 2)
accion_volver_casa = Accion("Volver a casa", 3)

# Definimos el estado actual, inicialmente vacío
estado_actual = set()

# Creamos una instancia de VigilanciaReplanificacion y ejecutamos el plan
vigilancia_replanificacion = VigilanciaReplanificacion([accion_ir_comprar, accion_comprar, accion_volver_casa], estado_actual)
vigilancia_replanificacion.ejecutar_plan()
