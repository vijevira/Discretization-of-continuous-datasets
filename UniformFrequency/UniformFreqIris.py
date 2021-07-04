'''
4th year Project
Topic - Implementation of Uniform Frequency Discretizer using Iris dataset
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

def tryX(arr,m):
  s=arr[::]
  s.sort()
  for i in range (0,len(s),len(s)//m):
    print(sum(s[i:i+len(s)//m])/(len(s)//m))

tryX(sepal_l,11)

'''
#function for uniform frequency discretizer
def equiFreq(sepal_l,m):
  data=sepal_l[::]
  data.sort()
  bins=[]
  for i in range (0,len(data),len(sepal_l)//m):
    bins.append(data[i])
  diff={}

  for i in range (len(bins)-1):
    diff[(bins[i],bins[i+1])]=round((bins[i]+bins[i+1])/2,2)
  desc=[]
  for i in sepal_l:
    for j in diff:
      if i>=bins[-1]:
        desc.append(bins[-1])
        break
      if j[0]<=i<j[1]:
        desc.append(diff[j])
  return [bins,desc]

#to print cut points of every attributes
def printCutPoints(arr,atrbNum):
    for i in range (len(arr)):
        print("Cut point", i , "of attribute" , atrbNum , ":",  arr[i])
    print("Number of cut points of attribute", atrbNum, ":", len(arr)-2,"\n")


#dicretize all values of attributes
w,x,y,z=equiFreq(sepal_l,10), equiFreq(sepal_w,10), equiFreq(petal_l,10),equiFreq(petal_w,10)

#printing cut points of every attributes
print("\n----------------------------------------------\n")
print("cut points of every attributes")
print("\n----------------------------------------------\n")
printCutPoints(w[0],1)
printCutPoints(x[0],2)
printCutPoints(y[0],3)
printCutPoints(z[0],4)

#list for saving all discretized values
descFreqIris=[]

for i,j,k,l in zip(w[1],x[1],y[1],z[1]):
  descFreqIris.append([i,j,k,l])

#print results
print("\n----------------------------------------------\n")
print("updated values of iris dataset")
print("\n----------------------------------------------\n")
#for i in range (len(descFreqIris)):
#    print(descFreqIris[i],target_name[target[i]])
'''
