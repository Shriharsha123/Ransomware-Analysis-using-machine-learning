'''
Author: Shriharsha
The following code is a python script to take as input the occurence
of IOCs in various ransomwares, then compute a score for each of the
IoCS
Version 0.9: All features implemented
Note: Requires data in text file to run
Noticed bugs:
NULL
''' 
import matplotlib.pyplot as plt 
import numpy as np 
import math 

#Initializing values
RansomwareNames=[]
IOCs=[]
weights=[]
IOC_Occurences=[]
with open('ransomnames.txt','r') as f:
    for i in f.read().split('\n'):
        RansomwareNames.append(i)

with open('iocs.txt','r') as f:
    for i in f.read().split('\n'):
        IOCs.append(i)

with open('weights.txt','r') as f:
    for i in f.read().split('\n'):
        weights.append(int(i))

with open('IOCoccurences.txt','r') as f:
    row=[i for i in f.read().split('\n')]
    for i in range(len(row)):
        IOC_Occurences.append([int(i) for i in row[i].split(' ')])
   
n=len(IOCs)
#The scores are respectively calculated as the following matrix/vector product: Scores= IOC_Occurences*(Weights)^T
sum=0
Scores=[]
for i in range(len(IOCs)):
    for j in range(len(RansomwareNames)):
        sum=sum + (IOC_Occurences[j][i]*weights[i])
    Scores.append(sum)
    sum=0

#Apply Sigmoid function on the scores
z =[ 1/(1 + np.exp(-x)) for x in Scores]
percentage=[100*x for x in z]

indexes=[i for i in range(n)]
for i in range(n-1):
    for j in range(i+1,n):
        if Scores[i]<Scores[j]:
            Scores[i] , Scores[j] = Scores[j] , Scores[i]
            indexes[i], indexes[j] = indexes[j] , indexes[i]
            z[i] , z[j] = z[j] , z[i]

plt.plot(Scores, z) 
plt.xlabel("Score") 
plt.ylabel("Sigmoid(score)") 
plt.show() 
print("Ransomwares ranked by scores:")
for i in range(n):
    print(IOCs[indexes[i]],": ",percentage[indexes[i]])