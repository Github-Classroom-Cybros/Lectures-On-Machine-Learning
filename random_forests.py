# RandomForests Classifier

from sklearn.ensemble import RandomForestClassifier


features = [[0, 0], [1, 1]]
labels = [0, 1]

clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit( features, labels)    # fitting data into the model (training)

print(clf.predict([[2., 2.]]))  # prediction (testing)
print(clf.predict([[58,5.6]]))
