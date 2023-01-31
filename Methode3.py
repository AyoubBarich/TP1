from random import randint
import math
Array=[]
def GenerateRandomArray(size,lowerBound,upperBound):  
    Array=[randint(lowerBound,upperBound) for i in range(size)]
    return Array


def GetSubArray(Array:list,firstIndex,lastIndex):
    sub=list[int]
    if (firstIndex==lastIndex):
        return Array[firstIndex]
    sub=[Array[i] for i in range(firstIndex,lastIndex)]
    return sub


def Somme(Array):
    Sum=0

    if isinstance(Array,list):
        for i in Array:
            Sum+=i
        print(Sum)
        return Sum
    
    return Array
    



def MaximalSubSequence(Array:list):
    lenght=len(Array)
    rightSubsequenceMax=[0,0]
    leftSubsequenceMax=[pointer,pointer]
    
    sum=Array[0]
    pointer=lenght//2
    tmp=0
    for i in range(0,pointer):
        tmp=0
        for j in range (i,pointer):
            tmp+=Array[j]
            if(sum < tmp):
                sum=tmp
                rightSubsequenceMax=[i,j]
    for i in range(pointer,len):
        tmp=0
        for j in range (i,len):
            tmp+=Array[j]
            if(sum < tmp):
                sum=tmp
                leftSubsequenceMax=[i,j]
    return rightSubsequenceMax if Somme(leftSubsequenceMax)<Somme(rightSubsequenceMax) else leftSubsequenceMax




########TEST########
MaximalSubSequence(GenerateRandomArray(500,-10,10))