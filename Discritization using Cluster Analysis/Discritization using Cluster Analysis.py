'''
4th year Project
Topic - Implementation of Cluster Analysis Discretizer
Group Members:
Vijendra Kumar (20171039)
Bhanu Pratap Shahi (20171031)
Vikash Kumar (20171038)
'''

#importing required library
#Use pip to install if it's not intsalled in your computer
import pandas as pd
import numpy as np
from sklearn.preprocessing import KBinsDiscretizer
#importing dataset
print("Enter full path of Dataset")
path=input()
data = pd.read_csv(path)

#adding all attributes in a list and converting it to numpy array
atrb=[]
atrbNames=[]

for i in data:
    atrb.append(data[i])
    atrbNames.append(i)

#print information regarding inputed dataset
print("Reading Dataset...")
print("Numbers of attributes in datasets = ",len(atrbNames))
print("Attrinutes Names are given below")
print(*atrbNames,sep="\n")
print("Numbers of columns = ", len(atrb[0]))

print("_______________")
print("enter numbers of bins for every attributes")
k=list(map(int,input().split()))
#function for cluster analysis discretizer

def clustering(X,k):
    est = KBinsDiscretizer(n_bins=k, encode='ordinal', strategy='quantile')
    X=X.values.reshape(-1,1) 
    Xt = est.fit_transform(X) 
    value=list(est.inverse_transform(Xt))
    return value
#to print cut points of every attributes
def printCutPoints(arr,atrbNum):
    for i in range (len(arr)):
        print("Cut point", i , "of attribute" , atrbNum , ":",  arr[i])
    print("Number of cut points of attribute", atrbNum, ":", len(arr),"\n")


#dicretize all values of attributes
discreteValues=[]
cutPoints=[]
for i in range (len(atrb)-1):
    atrbValues=atrb[i]
    temp=clustering(atrbValues,k[i])
    discreteValues.append(temp)
    #cutPoints.append(list(set(list(temp))))

for i in discreteValues:
    temp=set()
    for j in i:
      for k in j:
        temp.add(k)
    cutPoints.append(list(temp))
#printing cut points of every attributes
print("\n----------------------------------------------\n")
print("cut points of every attributes")
print("\n----------------------------------------------\n")
for i in range (len(cutPoints)):
    printCutPoints(cutPoints[i],i)


"""
#list for saving all discretized values
descIris=[[discreteValues[i][j] for i in range (len(discreteValues))] for j in range (len(discreteValues[0]))]
 #For Testing
#print the results
print("\n----------------------------------------------\n")
print("updated values of iris dataset")
print("\n----------------------------------------------\n")
for i in range (len(descIris)):
    print(descIris[i],atrb[-1][i])
"""
