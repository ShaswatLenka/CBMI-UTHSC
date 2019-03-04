from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Building a simple model

iris = datasets.load_iris()
X = iris.data
y = iris.target
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Random Forest classifier
rfc = RandomForestClassifier(n_estimators=100, n_jobs=2)
rfc.fit(X_train, y_train)

print("Accuracy = %0.2f" % accuracy_score(y_test, rfc.predict(X_test)))
print(classification_report(y_test, rfc.predict(X_test)))
