class MejorHipotesisActual:
    def __init__(self):
        self.hipotesis = None
        self.precision = 0.0

    def actualizar(self, nueva_hipotesis, nueva_precision):
        if nueva_precision > self.precision:
            self.hipotesis = nueva_hipotesis
            self.precision = nueva_precision
            print("Mejor hipótesis actualizada:", self.hipotesis)
            print("Nueva precisión:", self.precision)
        else:
            print("La nueva hipótesis no supera a la mejor actual.")

# Ejemplo de uso
bch = MejorHipotesisActual()

# Supongamos que hemos estado entrenando un clasificador y obtenemos una nueva hipótesis y precisión
nueva_hipotesis = "Clasificador SVM"
nueva_precision = 0.85

# Actualizar la mejor hipótesis actual con la nueva información
bch.actualizar(nueva_hipotesis, nueva_precision)

# Supongamos que obtenemos otra nueva hipótesis y precisión
otra_nueva_hipotesis = "Clasificador KNN"
otra_nueva_precision = 0.78

# Actualizar la mejor hipótesis actual con la otra nueva información
bch.actualizar(otra_nueva_hipotesis, otra_nueva_precision)
