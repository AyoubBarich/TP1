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

def Somme(T,d,f):
    if f<d:
        return -1
    if isinstance(T,list):
        sum =Somme(T,d,f-1)+T[f]
        return sum
    return T

def main(Array:list):
    sousSequenceMaximal=[0,0]
    sum=Array[0]
    print(Array)
    for i in range(len(Array)):      
        for j in range(i,len(Array)): 
            if(Somme(GetSubArray(Array,i,j),i,j) > sum):
                sum=Somme(GetSubArray(Array,i,j),i,j)
                #print("my sub array",GetSubArray(Array,i,j))
                sousSequenceMaximal=[i,j]
    print(sousSequenceMaximal)
    return sousSequenceMaximal




########TEST########
main(GenerateRandomArray(5,-10,10))