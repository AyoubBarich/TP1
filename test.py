
from random import randint


def Somme(Array):
    Sum=0

    if isinstance(Array,list):
        for i in Array:
            Sum+=i
        print(Sum)
        return Sum
    
    return Array
    


def Somme2(T,d,f):  
     if isinstance(T,list):
         if d>f:
             return 0
         sum =Somme2(T,d,f-1)+T[f]
         print(sum)
         return sum
     
     return T

def GenerateRandomArray(size,lowerBound,upperBound):  
    Array=[randint(lowerBound,upperBound) for i in range(size)]
    return Array
print("Strated")
#Somme(GenerateRandomArray(10000000,-10,10))
Somme2(GenerateRandomArray(10000000,-10,10),0,10000000)