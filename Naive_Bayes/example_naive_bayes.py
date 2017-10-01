# Michelle Morales
# Digital Ocean Tutorial - How to Build a Machine Learning Classifier in Python with Scikit-learn
# https://www.digitalocean.com/community/tutorials/how-to-build-a-machine-learning-classifier-in-python-with-scikit-learn


from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

# Load dataset
data = load_breast_cancer()

# Organize our data
label_names = data['target_names']
labels = data['target']
feature_names = data['feature_names']
features = data['data']

# Look at our data
print (label_names)
print ('Class label = ', labels[0])
print (feature_names)
print (features[0])

# Split our data
train, test, train_labels, test_labels = train_test_split(features, labels,
                                                          test_size=0.33, random_state=42)
# Initialize our classifier
gnb = GaussianNB()

# Train our classifier
model = gnb.fit(train, train_labels)

# Make predictions
preds = gnb.predict(test)
print(preds)

# Evaluate accuracy
print (accuracy_score(test_labels, preds))
