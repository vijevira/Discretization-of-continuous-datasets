'''
4th year Project
Topic - Implementation of Uniform Width Discretizer
Group Members:
Vijendra Kumar (20171039)
Bhanu Pratap Shahi (20171031)
Vikash Kumar (20171038)
'''

#importing required library
#Use pip to install if it's not intsalled in your computer
import pandas as pd
import numpy as np

#importing dataset
print("Enter full path of Dataset")
path=input()
data = pd.read_csv(path)

#adding all attributes in a list and converting it to numpy array
atrb=[]
atrbNames=[]
for i in data:
    atrb.append(data[i].to_numpy())
    atrbNames.append(i)

#print information regarding inputed dataset
print("Reading Dataset...")
print("Numbers of attributes in datasets = ",len(atrbNames))
print("Attrinutes Names are given below")
print(*atrbNames,sep="\n")
print("Numbers of columns = ", len(atrb[0]))


#function for uniform width discretizer
def equiWidth(arr1, m):
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
        print("Cut point", i-1 , "of attribute" , atrbNum , ":",  arr[i])
    print("Number of cut points of attribute", atrbNum, ":", len(arr)-2,"\n")


#dicretize all values of attributes
discreteValues=[]
cutPoints=[]
for i in range (len(atrb)-1):
    atrbValues=atrb[i]
    temp=equiWidth(atrbValues,10)
    discreteValues.append(temp[1])
    cutPoints.append(temp[0])


#printing cut points of every attributes
print("\n----------------------------------------------\n")
print("cut points of every attributes")
print("\n----------------------------------------------\n")
for i in range (len(cutPoints)):
    printCutPoints(cutPoints[i],i)

'''
#list for saving all discretized values
descIris=[[discreteValues[i][j] for i in range (len(discreteValues))] for j in range (len(discreteValues[0]))]

 #For Testing
#print the results
print("\n----------------------------------------------\n")
print("updated values of iris dataset")
print("\n----------------------------------------------\n")
for i in range (len(descIris)):
    print(descIris[i],atrb[-1][i])
'''
