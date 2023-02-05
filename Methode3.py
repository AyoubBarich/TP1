from random import randint
import math
Array=[]
#Generate a random array with a given size , a lower bound and an upper bound for the elements of the array
def GenerateRandomArray(size,lowerBound,upperBound):  
    Array=[randint(lowerBound,upperBound) for i in range(size)]
    return Array
#returns the sum of all the elements in the given array ,the first index and the last index
def Methode3(Array,d,f):
    
    if d==f:        #we check if the array has one element wich means it s sum is the element it self
        return [Array[d],d,f]
    if (f-d==1):    #if the given array has two element our max sum denpends on there sign
        
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
    #intiliazing 
    midPoint = (d+f)//2
    sumTemp = Array[midPoint]
    sumMax = sumTemp
    #we apply our function on the left and right sub arrays that do not contain the midpoint element
    ArrayLeft=Methode3(Array,d,midPoint-1)
    ArrayRight=Methode3(Array,midPoint+1,f)

   
    #we intiliaze our left sub sequence 
    sumArrayLeft = Array[midPoint]
    sumArrayLeftMax = sumArrayLeft
    leftIndexMax = midPoint
    
    #we go through all possible subsequences of our left array , calculate there max sum ad take note of our current index
    for leftIndex in range(midPoint-1,d-1,-1):
        sumArrayLeft+=Array[leftIndex]
        if(sumArrayLeftMax<= sumArrayLeft):
            sumArrayLeftMax=sumArrayLeft
            leftIndexMax=leftIndex

    #we intiliaze our right sub sequence 
    sumArrayRight = Array[midPoint]
    sumArrayRightMax = sumArrayRight
    rightIndexMax = midPoint

    #we go through all possible subsequences of our right array , calculate there max sum ad take note of our current index
    for rightIndex in range(midPoint+1,f+1):
            sumArrayRight+=Array[rightIndex]
            if(sumArrayRightMax<= sumArrayRight):
                sumArrayRightMax=sumArrayRight
                rightIndexMax=rightIndex

    #we sumMax is the max sum of the elements of the current subsequence with the midpoint included
    sumMax = sumArrayRightMax+sumArrayLeftMax-Array[midPoint]

    #we check wich of our summs is bigger and we return it s indexes in our first array
    if ArrayRight[0] < ArrayLeft[0] and sumMax<ArrayLeft[0]:
        
        return ArrayLeft
    elif ArrayLeft[0] < ArrayRight[0] and sumMax<ArrayRight[0]:
        
        return ArrayRight
    else:
        
        return [sumMax,leftIndexMax,rightIndexMax]


def Main(Array):
    return Methode3(Array,0,len(Array)-1)
    
########TEST########
print(Main(GenerateRandomArray(100,-10,10)))