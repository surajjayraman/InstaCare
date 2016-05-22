# -*- coding: utf-8 -*-
"""
Created on Sat May 07 07:09:40 2016

@author: Suraj
"""

import numpy as np
from sklearn.datasets import load_iris
from sklearn import tree


iris = load_iris()
test_idx = [0.50,100]
#print iris.feature_names
#print iris.target_names
#print iris.data[99]
#print iris.target[99]



#print entire data set
#for i in range(len(iris.target)):
   # print "Example %d: label %s, features %s" % (i, iris.target[i], iris.data[i])

#training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

#testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

clf = tree.DecisionTreeClassifier()
clf.fit(train_data,train_target)

print test_target

print clf.predict(test_data)

print iris.data[50], iris.target[50]

print iris.feature_names, iris.target_names