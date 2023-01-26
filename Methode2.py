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

def main(Array:list):
    sousSequenceMaximal=[]
    sum=0
    print(Array)

    for i in range(len(Array)-1): 
        
        for j in range(i+1,len(Array) ): 
            
            if(Somme(Array,i,j) > sum):
                sum=Somme(Array,i,j)
                print("my sub array",GetSubArray(Array,i,j))
                sousSequenceMaximal=[i,j]

                
    print(sousSequenceMaximal)           
    return sousSequenceMaximal


########TEST########
main(GenerateRandomArray(5,-10,10))