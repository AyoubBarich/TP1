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
        
        return Sum
    
    return Array
    




#def MaximalSubSequence(Array:list):
    print(Array)
    lenght = len(Array)
    pointer = lenght//2
    print(pointer)
    sousSequenceMaximal=[pointer,pointer]
    sum = Array[pointer]
    sumRight=Array[pointer]
    sumLeft=Array[0]
    leftSubsequence = GetSubArray(Array,0,pointer)
    rightSubsequence = GetSubArray(Array,pointer,lenght)

    if lenght>1:
        sousSequenceMaximalRight=MaximalSubSequence(rightSubsequence)
        sousSequenceMaximalLeft=MaximalSubSequence(leftSubsequence)


        if Somme(leftSubsequence)> sum:
            sumLeft = Somme(leftSubsequence)
            
            print("left sum :",sumLeft)
            

        if Somme(rightSubsequence)> sum :
            sumRight = Somme(rightSubsequence)
            pointer= lenght-pointer
            print("right sum :",sumRight)
        
        sum = max(sumRight,sumLeft)
        print("SummMax : ",sum)

        if sumLeft>sumRight :
            print("Array :", Array,"lenght :",lenght,"Sum :",sum,"SousMax :",sousSequenceMaximalLeft)
            #sousSequenceMaximalLeft = [lenght,lenght]
            return sousSequenceMaximalLeft
        else: 
            print("Array :", Array,"lenght :",lenght,"Sum :",sum,"SousMax :",sousSequenceMaximalRight)
            #sousSequenceMaximalRight=[pointer,pointer]
            return sousSequenceMaximalRight
    else:
        return sousSequenceMaximal
            
def MaxSub(Array,d,f):
    print(Array)
    if d==f:
        return [Array[d],d,f]
    if (f-d==1):
        
        if Array[d]>0 and Array[f]>0:
            return[Array[d]+Array[f],d,f]
        elif Array[d]>0:
            return [Array[d],d,d]
        elif Array[f]>0:
            return [Array[f],f,f]
        elif Array[d]>Array[f]:
            return[Array[d],d,d]
        else:
            return [Array[f],f,f]

    midPoint = (d+f)//2
    sumTemp = Array[midPoint]
    sumMax = sumTemp

    ArrayLeft=MaxSub(Array,d,midPoint-1)
    ArrayRight=MaxSub(Array,midPoint+1,f)
    print("left",ArrayLeft)
    print("right",ArrayRight)

    sumArrayLeft = Array[midPoint]
    sumArrayLeftMax = sumArrayLeft
    leftIndexMax = midPoint

    for leftIndex in range(midPoint-1,d-1,-1):
        sumArrayLeft+=Array[leftIndex]
        if(sumArrayLeftMax<= sumArrayLeft):
            sumArrayLeftMax=sumArrayLeft
            leftIndexMax=leftIndex

    sumArrayRight = Array[midPoint]
    sumArrayRightMax = sumArrayRight
    rightIndexMax = midPoint

    for rightIndex in range(midPoint+1,f+1):
            sumArrayRight+=Array[rightIndex]
            if(sumArrayRightMax<= sumArrayRight):
                sumArrayRightMax=sumArrayRight
                leftIndexMax=leftIndex


    sumMax = sumArrayRightMax+sumArrayLeftMax-Array[midPoint]

    if ArrayRight[0] < ArrayLeft[0] and sumMax<ArrayLeft[0]:
        
        return ArrayLeft
    elif ArrayLeft[0] < ArrayRight[0] and sumMax<ArrayRight[0]:
        
        return ArrayRight
    elif ArrayLeft[0] < sumMax  and sumMax>ArrayRight[0]:
        
        return [sumMax,leftIndexMax,rightIndexMax]



    
########TEST########
print(MaxSub([-3, -10, 6, 2, 10],0,4))