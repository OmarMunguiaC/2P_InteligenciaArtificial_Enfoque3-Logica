import numpy as np

class KDecisionList:
    def __init__(self, k):
        self.k = k
        self.rules = []

    def fit(self, X, y):
        for i in range(self.k):
            rule = (X[i], y[i])
            self.rules.append(rule)

    def predict(self, X):
        for rule in self.rules:
            condition, prediction = rule
            if condition == X:
                return prediction
        return None  # Si no se encuentra una regla que se ajuste, devuelve None

class TreeNode:
    def __init__(self, k):
        self.k = k
        self.attribute = None
        self.children = {}

    def build(self, X, y):
        if len(X) <= self.k:
            self.attribute = max(set(y), key=y.count)
            return

        best_attribute = None
        best_threshold = None
        best_gini = float('inf')

        for i in range(len(X[0])):
            for value in set(X[:, i]):
                left_indices = [index for index, val in enumerate(X[:, i]) if val <= value]
                right_indices = [index for index, val in enumerate(X[:, i]) if val > value]

                left_labels = y[left_indices]
                right_labels = y[right_indices]

                gini_left = self.gini_impurity(left_labels)
                gini_right = self.gini_impurity(right_labels)

                gini = (len(left_indices) / len(y)) * gini_left + (len(right_indices) / len(y)) * gini_right

                if gini < best_gini:
                    best_gini = gini
                    best_attribute = i
                    best_threshold = value

        self.attribute = (best_attribute, best_threshold)

        left_indices = [index for index, val in enumerate(X[:, best_attribute]) if val <= best_threshold]
        right_indices = [index for index, val in enumerate(X[:, best_attribute]) if val > best_threshold]

        if left_indices:
            self.children["<= {}".format(best_threshold)] = TreeNode(self.k)
            self.children["<= {}".format(best_threshold)].build(X[left_indices], y[left_indices])
        if right_indices:
            self.children["> {}".format(best_threshold)] = TreeNode(self.k)
            self.children["> {}".format(best_threshold)].build(X[right_indices], y[right_indices])

    def predict(self, sample):
        if self.attribute is None:
            return None

        attribute, threshold = self.attribute

        if sample[attribute] <= threshold:
            if "<= {}".format(threshold) in self.children:
                return self.children["<= {}".format(threshold)].predict(sample)
        else:
            if "> {}".format(threshold) in self.children:
                return self.children["> {}".format(threshold)].predict(sample)

        return max(set(y), key=y.count)

    def gini_impurity(self, labels):
        classes = set(labels)
        gini = 1.0
        for c in classes:
            gini -= (sum(labels == c) / len(labels)) ** 2
        return gini

# Ejemplo de uso de KDecisionList
X_train_list = [[1, 0, 1], [0, 1, 1], [1, 1, 0]]
y_train_list = ['A', 'B', 'C']

model_list = KDecisionList(k=3)
model_list.fit(X_train_list, y_train_list)

X_test_list = [1, 0, 1]
prediction_list = model_list.predict(X_test_list)
print("Predicción KDecisionList:", prediction_list)

# Ejemplo de uso de TreeNode
X_train_tree = np.array([[1, 2], [2, 3], [3, 4], [4, 5], [5, 6]])
y_train_tree = np.array([1, 0, 1, 0, 1])

tree = TreeNode(k=2)
tree.build(X_train_tree, y_train_tree)

sample_tree = [3, 4]
prediction_tree = tree.predict(sample_tree)
print("Predicción TreeNode:", prediction_tree)
