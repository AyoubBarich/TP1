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

def Somme(Array:list):
    Sum=0
    for i in Array:
        Sum+=i
    return Sum

    



def main(Array:list):
    sousSequenceMaximal=[]
    sum=0
    print(Array)
    for i in range(len(Array)): 
        
        for j in range(i+1,len(Array)  ): 
            
            if(Somme(GetSubArray(Array,i,j)) > sum):
                sum=Somme(GetSubArray(Array,i,j))
                print("my sub array",GetSubArray(Array,i,j))
                sousSequenceMaximal=[i,j]
    return sousSequenceMaximal




########TEST########
main(GenerateRandomArray(5,-10,10))

