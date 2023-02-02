from random import randint
Array=[]
def GenerateRandomArray(size,lowerBound,upperBound):  
    Array=[randint(lowerBound,upperBound) for i in range(size)]
    return Array


def GetSubArray(Array:list,firstIndex,lastIndex):
    sub=list[int]
    if (firstIndex==lastIndex):
        return Array[firstIndex]
    sub=[Array[i] for i in range(firstIndex,lastIndex+1)]
    return sub

def main(Array:list):
    sousSequenceMaximal=[0,0]
    sum=Array[0]
    tmp =0
    #print(Array)
    for i in range(len(Array)): 
        tmp=0     
        for j in range(i,len(Array)): 
            
            tmp+=Array[j]
            #print(i,j,tmp,GetSubArray(Array,i,j))
            if(sum < tmp):
                sum=tmp
                #print("my sub array",GetSubArray(Array,i,j))
                sousSequenceMaximal=[i,j]
    print(sousSequenceMaximal)
    return sousSequenceMaximal




########TEST########
main(GenerateRandomArray(1000,-10,10))