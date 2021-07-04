'''
4th year Project
Topic - Implementation of Uniform Width Discretizer using Iris dataset
Group Members:
Vijendra Kumar (20171039)
Bhanu Pratap Shahi (20171031)
Vikash Kumar (20171038)
'''

#importing required library
#Use pip to install if it's not intsalled in your computer
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing iris dataset
data = load_iris()
target=data.target
target_name=data.target_names
df = pd.DataFrame(data.data, columns=data.feature_names)

#initializing variables for every attributes
df_sepal_l=df['sepal length (cm)']
df_sepal_w=df['sepal width (cm)']
df_petal_l=df['petal length (cm)']
df_petal_w=df['petal width (cm)']

#converting attributes into numpy array 
sepal_l=df_sepal_l.to_numpy()
sepal_w=df_sepal_w.to_numpy()
petal_l=df_petal_l.to_numpy()
petal_w=df_petal_w.to_numpy()




#function for uniform width discretizer
def equiwidth(arr1, m):
    a = len(arr1)
    w = ((max(arr1) - min(arr1)) / m)
    min1 = min(arr1)
    arr = []
    for i in range(0, m + 1):
        arr = arr + [min1 + w * i]
    arr2=[]
    for i in arr1:
      index=int((i-min1)/w)
      arr2.append(round(arr[index],2))
    return [arr,arr2]

#to print cut points of every attributes
def printCutPoints(arr,atrbNum):
    for i in range (1,len(arr)-1):
        print("Cut point", i , "of attribute" , atrbNum , ":",  arr[i])
    print("Number of cut points of attribute", atrbNum, ":", len(arr)-2,"\n")

#dicretize all values of attributes
w,x,y,z=equiwidth(sepal_l,10), equiwidth(sepal_w,10), equiwidth(petal_l,10),equiwidth(petal_w,10)


#printing cut points of every attributes
print("\n----------------------------------------------\n")
print("cut points of every attributes")
print("\n----------------------------------------------\n")
printCutPoints(w[0],1)
printCutPoints(x[0],2)
printCutPoints(y[0],3)
printCutPoints(z[0],4)

#list for saving all discretized values
descIris=[]
for i,j,k,l in zip(w[1],x[1],y[1],z[1]):
  descIris.append([i,j,k,l])

#print the results
print("\n----------------------------------------------\n")
print("updated values of iris dataset")
print("\n----------------------------------------------\n")
for i in range (len(descIris)):
    print(descIris[i],target_name[target[i]])
