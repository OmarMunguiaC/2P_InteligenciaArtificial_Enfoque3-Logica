import numpy as np

class NodoRegresion:
    def __init__(self, atributo=None, valor=None, resultado=None):
        self.atributo = atributo
        self.valor = valor
        self.resultado = resultado
        self.hijos = {}

class M5:
    def __init__(self, min_muestras=2):
        self.min_muestras = min_muestras

    def calcular_varianza(self, datos):
        if len(datos) == 0:
            return 0
        return np.var(datos[:, -1])

    def calcular_error_absoluto_medio(self, datos, valor_predicho):
        return np.mean(np.abs(datos[:, -1] - valor_predicho))

    def construir_arbol_regresion(self, datos, atributos):
        if len(datos) < self.min_muestras:
            return NodoRegresion(resultado=np.mean(datos[:, -1]))

        varianza_padre = self.calcular_varianza(datos)
        mejor_varianza_reducida = float('inf')
        mejor_atributo = None
        mejor_valor = None

        for atributo in atributos:
            valores_atributo = np.unique(datos[:, atributo])
            for valor in valores_atributo:
                datos_izquierda = datos[datos[:, atributo] <= valor]
                datos_derecha = datos[datos[:, atributo] > valor]

                if len(datos_izquierda) == 0 or len(datos_derecha) == 0:
                    continue

                varianza_izquierda = self.calcular_varianza(datos_izquierda)
                varianza_derecha = self.calcular_varianza(datos_derecha)
                varianza_reducida = (len(datos_izquierda) / len(datos)) * varianza_izquierda + (len(datos_derecha) / len(datos)) * varianza_derecha

                if varianza_reducida < mejor_varianza_reducida:
                    mejor_varianza_reducida = varianza_reducida
                    mejor_atributo = atributo
                    mejor_valor = valor

        if varianza_padre - mejor_varianza_reducida < 0.0001:
            return NodoRegresion(resultado=np.mean(datos[:, -1]))

        arbol_regresion = NodoRegresion(mejor_atributo, mejor_valor)
        datos_izquierda = datos[datos[:, mejor_atributo] <= mejor_valor]
        datos_derecha = datos[datos[:, mejor_atributo] > mejor_valor]
        nuevos_atributos = [atributo for atributo in atributos if atributo != mejor_atributo]

        arbol_regresion.hijos['izquierda'] = self.construir_arbol_regresion(datos_izquierda, nuevos_atributos)
        arbol_regresion.hijos['derecha'] = self.construir_arbol_regresion(datos_derecha, nuevos_atributos)

        return arbol_regresion

    def predecir(self, arbol, muestra):
        if arbol.resultado is not None:
            return arbol.resultado

        hijo = arbol.hijos['izquierda'] if muestra[arbol.atributo] <= arbol.valor else arbol.hijos['derecha']
        return self.predecir(hijo, muestra)

# Ejemplo de uso
datos = np.array([
    [5, 20],
    [7, 25],
    [10, 30],
    [15, 35],
    [20, 40]
])

atributos = [0]  # Único atributo en este ejemplo

m5 = M5(min_muestras=1)
arbol_regresion = m5.construir_arbol_regresion(datos, atributos)

# Predecir para una muestra de prueba
muestra_prueba = [12]  # Valor del atributo para la muestra de prueba
prediccion = m5.predecir(arbol_regresion, muestra_prueba)
print("Predicción para la muestra de prueba:", prediccion)
