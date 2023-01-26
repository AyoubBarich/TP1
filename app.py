#creer un tableaux entiers reltifs aleatoires 
#question 1 double boucle
#definir la fonction somme 
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


    



def main (Array:list):
    print(Array)
    result=0
    for i in range(len(Array)): 
        print(i)
        for j in range(i+1,len(Array)  ): 
            print(j)
            if(sum(GetSubArray(Array,i,j)) > result):
                result=sum(GetSubArray(Array,i,j))
                print("my sub array",GetSubArray(Array,i,j))
    return result
    



########TEST########


main(GenerateRandomArray(5,-10,10))
