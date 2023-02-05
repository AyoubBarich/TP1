
from random import randint
import time
import matplotlib.pyplot as plt
import math
import Methode1
import Methode2
import Methode3




###########################################TEST###########################################


#First test : we test the if the results of each function is compatible with the others

def TestCompatibility(testArray):
    lenght = len(testArray)-1
    methode1 = Methode1.Main(testArray)
    methode2 = Methode2.Main(testArray)
    methode3 = [Methode3.Main(testArray)[1],Methode3.Main(testArray)[2]]
    if methode1==methode2 and methode2==methode3:
        return True
    else:
        print(testArray,"methode 1: ",methode1,"methode 2: ",methode2,"methode 3: ",methode3)
        return False

def Tester(size,numberOftests):
    for i in range (numberOftests):
        print(TestCompatibility(Methode1.GenerateRandomArray(size,-10,10)))

#the tests that return false are due to arrays that can have two diffrent subsequences with the same max sum.
#Example:[3, -8, 9, 0, 0] wich accepts  [2, 2] and [2, 4]

#Second test : we plot the execution time of each function with a given array size

CONST=1000

def plotter(methode,sizeMax,step,color):
    
    Xcoord=[]
    Ycoord=[]
    for i in range(5,sizeMax,step):
        start = time.time()
        methode.Main(Methode1.GenerateRandomArray(i,-10,10))
        execTime = time.time()-start

        Xcoord.append(i)
        Ycoord.append(execTime*CONST)


    plt.xlabel("Taille de la liste")
    plt.ylabel("Temps")
    return plt.plot(Xcoord,Ycoord,color)

def complexityPlot(Method,Complexity,sizeMax,step):
    Xcoord=[]
    Ycoord=[]
    YcoordOfComplexity=[]
    for i in range(5,sizeMax,step):
        start = time.time()
        Method.Main(Methode1.GenerateRandomArray(i,-10,10))
        execTime = time.time()-start
        Xcoord.append(i)
        Ycoord.append(execTime*CONST)
        YcoordOfComplexity.append(Complexity(i)/CONST)

    plt.xlabel("Taille de la liste")
    plt.ylabel("Temps")
    return (plt.plot(Xcoord,YcoordOfComplexity,"b"),plt.plot(Xcoord,Ycoord,"r"))

def Cube(x):
    return x*x*x

def Square(x):
    return x*x

def NLog(x):
    return x*math.log2(x)
###########################################GRAPH###########################################



###########################################All Functions###########################################
plotter(Methode1,300,50,'b')
plotter(Methode2,1000,50,'r')
plotter(Methode3,1000,50,'g')
plt.show()
###########################################Methode1###########################################

# complexityPlot(Methode1,Cube,300,50)
# plt.show()

###########################################Methode2###########################################

# complexityPlot(Methode2,Square,2000,10)
# plt.show()

###########################################Methode3###########################################

# complexityPlot(Methode3,NLog,2000,10)
# plt.show()

