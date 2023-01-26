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

#def Somme(T:list,d,f):
#    if f<d:
#        return -1
#    sum =Somme(T,d,f-1)+T[f]
#    return sum
def Somme(Array):
    Sum=0
    if isinstance(Array,list):
        for i in Array:
            Sum+=i
        return Sum
    return Array


def SousSequenceMaximal(Array:list):
    sum=Array[0]
    pointer=math.floor(len(Array)/2)
    rightSousSequence=GetSubArray(Array,0,pointer)
    leftSousSequence=GetSubArray(Array,pointer,len(Array)-1)
    if(Somme(rightSousSequence) > sum):
                sum=Somme(rightSousSequence)
                print("my sub array",GetSubArray(Array,i,j))
                sousSequenceMaximal=[i,j]
