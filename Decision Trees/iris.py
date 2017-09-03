from sklearn.datasets import load_iris
import numpy as np
from sklearn import tree

iris = load_iris()
#print(iris.feature_names)
#print(iris.target_names)
#print(iris.data[0])
#print(iris.target[0])
'''for i in range(len(iris.target)):
	print("Features: %s Target: %s"%(iris.data[i],iris.target[i]))'''
test_idx = [0,50,100]

#training  data
train_data = np.delete(iris.data,test_idx,axis=0)
train_label = np.delete(iris.target,test_idx)

#testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]
clf = tree.DecisionTreeClassifier()
clf.fit(train_data,train_label)
print(clf.predict(test_data))
print(test_target)


import graphviz 
dot_data = tree.export_graphviz(clf, out_file=None) 
graph = graphviz.Source(dot_data) 
graph.render("iris") 

dot_data = tree.export_graphviz(clf, out_file=None, 
                         feature_names=iris.feature_names,  
                         class_names=iris.target_names,  
                         filled=True, rounded=True,  
                         special_characters=True)  
graph = graphviz.Source(dot_data)  
graph 
