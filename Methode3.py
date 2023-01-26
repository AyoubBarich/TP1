from random import randint
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

def Somme(T:list,d,f):
    if f<d:
        return -1
    sum =Somme(T,d,f-1)+T[f]
    return sum

def SousSequenceMaximal(Array:list):
    rightSousSequence=
