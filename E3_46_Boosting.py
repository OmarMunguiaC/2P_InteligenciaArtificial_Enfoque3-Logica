from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Cargar el conjunto de datos
iris = load_iris()
X = iris.data
y = iris.target

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un clasificador base (por ejemplo, un árbol de decisión)
clasificador_base = DecisionTreeClassifier(max_depth=1)

# Crear el clasificador AdaBoost
boosting = AdaBoostClassifier(base_estimator=clasificador_base, n_estimators=50, random_state=42)

# Entrenar el clasificador AdaBoost
boosting.fit(X_train, y_train)

# Hacer predicciones en el conjunto de prueba
predicciones = boosting.predict(X_test)

# Calcular la precisión
precision = accuracy_score(y_test, predicciones)
print("Precisión del clasificador AdaBoost:", precision)
