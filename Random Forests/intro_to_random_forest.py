
#RandomForests Classifier

from sklearn.ensemble import RandomForestClassifier


features = [[0, 0], [1, 1], [80,3], [56,5], [70,5], [45,1]]
labels = [0, 1, 1, 1, 1, 0]

clf = RandomForestClassifier(n_estimators=10)
# n_estimators (parameter) indicates number of trees included into our model 

clf = clf.fit( features, labels)    # fitting data into the model (training)

print(clf.predict([[2., 2.]]))  # prediction (testing)
print(clf.predict([[58,5]]))
