#creer un tableaux entiers reltifs aleatoires 
#question 1 double boucle
#definir la fonction somme 
from random import randint
Array=[]
def GenerateRandomArray(size,lowerBound,upperBound):
    for i in range(size):
        Array.append(randint(lowerBound,upperBound))
    return Array




def GetSubArray(Array:list,firstIndex,lastIndex):
    sub=list[int]
    for i in range(firstIndex,lastIndex):
        sub.append(Array[i])
    return sub


def Somme (Array:list):
    sum=0
    for i in Array:
        sum+=i
    return sum

GenerateRandomArray(5,-10,10)
print(Array)
result=0
for i in range(len(Array)):
    for j in range(len(Array)):
        if(Somme(GetSubArray(Array,i,j))>result):
            result=Somme(GetSubArray(Array,i,j))
            print("my sub array",GetSubArray(Array,i,j))
            print(result)

