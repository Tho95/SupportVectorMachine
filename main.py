# Thomas Hübscher / 08.02.2020
# Classification via SVM for iris dataset

from sklearn.datasets import load_iris
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

import dataInfo
import plot

# notes: C = Regularization; kernel transformation for better decision boundary
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
X['target'] = iris.target

plot.target(X) # shows equal number of unique target values

plot.count(X)
plot.scatter(X)
plot.swarm(X)

dataInfo.general(X)
dataInfo.missing_value_per_column(X)
dataInfo.colType(X)

y = X['target'] #(target we want to predict)
X.drop('target', axis = 1, inplace=True)

print(X.head())
print("target-values:", iris.target_names)

X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.6, test_size=0.4,random_state=9)

#####model
model = SVC(kernel='rbf',)

model.fit(X_train,y_train)
print("Score: ", model.score(X_valid, y_valid))
predictions = model.predict(X_valid)





