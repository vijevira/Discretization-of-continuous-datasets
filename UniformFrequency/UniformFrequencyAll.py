'''
4th year Project
Topic - Implementation of Uniform Frequency Discretizer
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
    for i in range (1,len(arr)):
        print("Cut point", i-1 , "of attribute" , atrbNum , ":",  arr[i])
    print("Number of cut points of attribute", atrbNum, ":", len(arr)-1,"\n")


#dicretize all values of attributes
discreteValues=[]
cutPoints=[]
for i in range (len(atrb)-1):
    atrbValues=atrb[i]
    temp=equiFreq(atrbValues,10)
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
