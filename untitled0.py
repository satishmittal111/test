# -*- coding: utf-8 -*-
"""
Created on Wed Feb 15 19:03:07 2017

@author: user
"""
x=['a','b','c']
y=[1,2,3]
l=len(x)
a=0
result={}
for s in x:
    result[x[a]] = y[a]
    a=a+1
    
#result={'a':1,'b':2,'c':3}
print result, l