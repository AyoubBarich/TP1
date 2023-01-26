from random import randint
class Array:


    def GenerateRandomArray(size,lowerBound,upperBound):    
        Array=[randint(lowerBound,upperBound) for i in range(size)]
        return Array




    def GetSubArray(Array:list,firstIndex,lastIndex):
        sub=list[int]
        if (firstIndex==lastIndex):
            return Array[firstIndex]
        sub=[Array[i] for i in range(firstIndex,lastIndex)]
        return sub