
from random import randint
Array=[]

#Generate a random array with a given size , a lower bound and an upper bound for the elements of the array
def GenerateRandomArray(size,lowerBound,upperBound):  
    Array=[randint(lowerBound,upperBound) for i in range(size)]
    return Array
#returns a sub array of a given array ,the first index and the last index 
def GetSubArray(Array:list,firstIndex,lastIndex): 
    if (firstIndex==lastIndex):
        return Array[firstIndex]
    sub=[Array[i] for i in range(firstIndex,lastIndex+1)]
    return sub
#returns the sum of all the elements in the given array
def Somme(Array):
    Sum=0
    if isinstance(Array,list):
        for i in Array:
            Sum+=i
        return Sum
    return Array

#returns the first and last index of the sub array correspondent to the maximum subsequence in the given array
def Main(Array:list):
    #intiliazing 
    sousSequenceMaximal=[0,0]                       
    sum=Array[0]                                     
    #the loop goes through all possible subsequences in the given array
    for i in range(len(Array)):                    
        for j in range(i,len(Array)):       
            #we calculate the sum of the elements in the current subsuquence  and if it s bigger than our sum we permute and keep note of our current index      
            if(Somme(GetSubArray(Array,i,j)) > sum):    
                sum=Somme(GetSubArray(Array,i,j))   
                sousSequenceMaximal=[i,j]               
    
    return sousSequenceMaximal




########TEST########
print(Main(GenerateRandomArray(100,-10,10)))

