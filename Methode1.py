#creer un tableaux entiers reltifs aleatoires 
#question 1 double boucle
#definir la fonction somme 
from random import randint
Array=[]
def GenerateRandomArray(size,lowerBound,upperBound):  
    Array=[randint(lowerBound,upperBound) for i in range(size)]
    return Array




def GetSubArray(Array:list,firstIndex,lastIndex): 
    if (firstIndex==lastIndex):
        return Array[firstIndex]
    sub=[Array[i] for i in range(firstIndex,lastIndex+1)]
    return sub

def Somme(Array):
    Sum=0

    if isinstance(Array,list):
        for i in Array:
            Sum+=i
        return Sum
    return Array

    



def main(Array:list):
    sousSequenceMaximal=[0,0]
    sum=Array[0]
    
    for i in range(len(Array)):      
        for j in range(i,len(Array)): 
            if(Somme(GetSubArray(Array,i,j)) > sum):
                sum=Somme(GetSubArray(Array,i,j))
                #print("my sub array",GetSubArray(Array,i,j))
                sousSequenceMaximal=[i,j]
    print(sousSequenceMaximal)
    return sousSequenceMaximal




########TEST########
main(GenerateRandomArray(500,-10,10))

