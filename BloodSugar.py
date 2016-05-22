# -*- coding: utf-8 -*-
"""
Created on Tue May 03 13:29:37 2016

@author: Suraj
"""

from sklearn import tree
#Blood Sugar Values as Features / Measurements 
features = [[110, 120],[120, 170],[150, 110],[170, 122]]
#labels =["Normal", "Normal", "Abnormal", "Abnormal"]
# Blood Value <= 120 is assigned Normal and represented by 0 else 1
labels =[0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print clf.predict([[160,120]])

#expected outcome is Abnormal hence will print 1