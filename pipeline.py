# -*- coding: utf-8 -*-
"""
Created on Sat May 14 19:11:20 2016

@author: Suraj
"""

from sklearn import datasets
iris = datasets.load_iris()


X = iris.data
y = iris.target

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .5)

#from sklearn import tree
#my_classifier = tree.DecisionTreeClassifier()

from sklearn.neighbors import KNeighborsClassifier
my_classifier = KNeighborsClassifier()

my_classifier.fit(X_train, y_train)

predictions = my_classifier.predict(X_test)
print predictions

print y_test