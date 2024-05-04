class TratamientoLogicoLenguaje:
    def __init__(self):
        self.reglas_semanticas = {}  # Reglas semánticas que pueden influir en la interpretación

    def interpretar_oracion(self, oracion):
        # Ejemplo de regla semántica: Juan es una persona y María es un perro
        self.reglas_semanticas["Juan"] = "persona"
        self.reglas_semanticas["María"] = "perro"

        # Interpretación 1: Juan ama a María
        interpretacion1 = self.interpretar("Ama(Juan, María)")

        # Interpretación 2: María ama a Juan
        interpretacion2 = self.interpretar("Ama(María, Juan)")

        # Determinar la interpretación más probable dada las reglas semánticas
        if interpretacion1 > interpretacion2:
            return "Juan ama a María"
        elif interpretacion1 < interpretacion2:
            return "María ama a Juan"
        else:
            return "La interpretación es ambigua"

    def interpretar(self, interpretacion):
        # Simular inferencia lógica utilizando reglas semánticas y contexto
        puntaje = 0
        for palabra in interpretacion.split("("):
            palabra = palabra.rstrip(")")
            if palabra in self.reglas_semanticas:
                puntaje += 1  # Incrementar el puntaje si la palabra está en las reglas semánticas
        return puntaje

# Ejemplo de uso
tratamiento_lenguaje = TratamientoLogicoLenguaje()
oracion = "Juan ama a María"
interpretacion = tratamiento_lenguaje.interpretar_oracion(oracion)
print("Interpretación de la oración:", interpretacion)
