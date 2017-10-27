from sklearn import tree
features = [[120, 0], [130, 0], [110, 1], [125, 1]]
labels = [0, 0, 1, 1]
t = tree.DecisionTreeClassifier()
t.fit(features, labels)
p = t.predict([[115,1],[110,0]])