from sklearn import tree

features  = [[80,5.6],[56,5.5],[70,5.2],[45,5.2]]
label = [1,0,1,0]

clf = tree.DecisionTreeClassifier()
clf.fit(features,label)
print(clf.predict([[100,5.9]]))
print(clf.predict([[58,5.6]]))
