from random import randint
Array=[]
#Generate a random array with a given size , a lower bound and an upper bound for the elements of the array
def GenerateRandomArray(size,lowerBound,upperBound):  
    Array=[randint(lowerBound,upperBound) for i in range(size)]
    return Array
#returns the first and last index of the sub array correspondent to the maximum subsequence in the given array
def Main(Array:list):
    lenght =len(Array)
    sousSequenceMaximal=[0,0]
    sum=Array[0]
    tmp =0
    #the loop goes through all possible subsequences in the given array
    for i in range(lenght): 
        tmp=0                       #we keep note of our sum using the variable tmp
        for j in range(i,lenght): 
            
            tmp+=Array[j]           #we calculate the sum of the current subsequence using the previous sum if it s bigger than our sum we permute and keep note of our current index
            if(sum < tmp):          
                sum=tmp
                sousSequenceMaximal=[i,j]
    return sousSequenceMaximal




########TEST########
print(Main(GenerateRandomArray(1000,-10,10)))