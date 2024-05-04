class SistemaReglas:
    def __init__(self, reglas):
        self.reglas = reglas

    def encadenamiento_hacia_adelante(self, hechos):
        while True:
            activaciones = False
            # Itera sobre todas las reglas en el sistema
            for regla, conclusion in self.reglas.items():
                # Verifica si todas las premisas de la regla están en los hechos
                if conclusion not in hechos and all(premisa in hechos for premisa in regla):
                    # Si se cumplen las condiciones, agrega la conclusión a los hechos
                    hechos.add(conclusion)
                    print(f"Se activó la regla: {regla} -> {conclusion}")
                    activaciones = True
            # Si no se activa ninguna regla en esta iteración, termina el ciclo
            if not activaciones:
                break
        return hechos

    def encadenamiento_hacia_atras(self, meta, hechos=set()):
        # Si la meta ya está en los hechos, retorna True
        if meta in hechos:
            return True
        # Itera sobre todas las reglas en el sistema
        for regla, conclusion in self.reglas.items():
            # Verifica si la conclusión de la regla coincide con la meta
            if conclusion == meta:
                # Verifica si todas las premisas de la regla se pueden probar recursivamente
                if all(self.encadenamiento_hacia_atras(premisa, hechos) for premisa in regla):
                    # Si todas las premisas se pueden probar, agrega la meta a los hechos y retorna True
                    hechos.add(meta)
                    print(f"Se activó la regla: {regla} -> {conclusion}")
                    return True
        # Si ninguna regla puede probar la meta, retorna False
        return False

# Ejemplo de uso
reglas = {
    ('p', 'q'): 'r',
    ('r', 's'): 't',
    ('t',): 'u',
    ('u',): 'v',
    ('v',): 'w'
}
sistema = SistemaReglas(reglas)

# Encadenamiento hacia adelante
print("Encadenamiento hacia adelante:")
hechos = sistema.encadenamiento_hacia_adelante(set(['p', 'q']))
print("Hechos:", hechos)

# Encadenamiento hacia atrás
print("\nEncadenamiento hacia atrás:")
meta = 'w'
resultado = sistema.encadenamiento_hacia_atras(meta)
print(f"¿Se puede probar la meta '{meta}'?: {resultado}")
