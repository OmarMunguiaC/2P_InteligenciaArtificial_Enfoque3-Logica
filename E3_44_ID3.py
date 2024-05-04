import numpy as np

class NodoDecision:
    def __init__(self, atributo=None, valor=None, resultado=None):
        self.atributo = atributo
        self.valor = valor
        self.resultado = resultado
        self.hijos = {}

class ID3:
    def __init__(self):
        pass

    def calcular_entropia(self, datos):
        _, counts = np.unique(datos[:, -1], return_counts=True)
        probabilidad = counts / len(datos)
        entropia = -np.sum(probabilidad * np.log2(probabilidad))
        return entropia

    def calcular_ganancia_informacion(self, datos, indice_atributo):
        entropia_total = self.calcular_entropia(datos)
        valores, counts = np.unique(datos[:, indice_atributo], return_counts=True)
        entropia_atributo = np.sum([(counts[i] / np.sum(counts)) * self.calcular_entropia(datos[datos[:, indice_atributo] == valores[i]]) for i in range(len(valores))])
        ganancia_informacion = entropia_total - entropia_atributo
        return ganancia_informacion

    def construir_arbol_decision(self, datos, atributos):
        if len(np.unique(datos[:, -1])) == 1:
            return NodoDecision(resultado=np.unique(datos[:, -1])[0])

        if len(atributos) == 0:
            return NodoDecision(resultado=np.argmax(np.unique(datos[:, -1], return_counts=True)[1]))

        mejor_atributo = np.argmax([self.calcular_ganancia_informacion(datos, i) for i in range(len(atributos))])
        arbol_decision = NodoDecision(atributos[mejor_atributo])

        valores_atributo = np.unique(datos[:, mejor_atributo])
        nuevos_atributos = [atributo for i, atributo in enumerate(atributos) if i != mejor_atributo]

        for valor in valores_atributo:
            subdatos = datos[datos[:, mejor_atributo] == valor]
            hijo = self.construir_arbol_decision(subdatos, nuevos_atributos)
            arbol_decision.hijos[valor] = hijo

        return arbol_decision

    def imprimir_arbol(self, nodo, nivel=0):
        if nodo.resultado is not None:
            print("  " * nivel + "Resultado:", nodo.resultado)
        else:
            print("  " * nivel + nodo.atributo)
            for valor, hijo in nodo.hijos.items():
                print("  " * (nivel + 1) + valor)
                self.imprimir_arbol(hijo, nivel + 2)

# Ejemplo de uso
datos = np.array([
    ['Soleado', 'Caliente', 'Alta', 'Débil', 'No'],
    ['Soleado', 'Caliente', 'Alta', 'Fuerte', 'No'],
    ['Nublado', 'Caliente', 'Alta', 'Débil', 'Sí'],
    ['Lluvioso', 'Templado', 'Alta', 'Débil', 'Sí'],
    ['Lluvioso', 'Frío', 'Normal', 'Débil', 'Sí'],
    ['Lluvioso', 'Frío', 'Normal', 'Fuerte', 'No'],
    ['Nublado', 'Frío', 'Normal', 'Fuerte', 'Sí'],
    ['Soleado', 'Templado', 'Alta', 'Débil', 'No'],
    ['Soleado', 'Frío', 'Normal', 'Débil', 'Sí'],
    ['Lluvioso', 'Templado', 'Normal', 'Débil', 'Sí'],
    ['Soleado', 'Templado', 'Normal', 'Fuerte', 'Sí'],
    ['Nublado', 'Templado', 'Alta', 'Fuerte', 'Sí'],
    ['Nublado', 'Caliente', 'Normal', 'Débil', 'Sí'],
    ['Lluvioso', 'Templado', 'Alta', 'Fuerte', 'No']
])

atributos = ['Outlook', 'Temperature', 'Humidity', 'Wind']

id3 = ID3()
arbol_decision = id3.construir_arbol_decision(datos, atributos)

print("Árbol de Decisión:")
id3.imprimir_arbol(arbol_decision)
