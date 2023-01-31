import random

def Maximum_tuple_first_element(T1, T2, T3):
  sum_max = max(T1[0],T2[0],T3[0])
  if (T1[0] == sum_max):
    return T1
  elif (T2[0] == sum_max):
    return T2
  else :
    return T3

def Method3(T):

  if (len(T) == 1):
    return (T[0], 0 , 0)
    
  else:
    m = len(T) // 2
    sum = T[m]
    ind_g = m 
    ind_d = m 
    
    while (ind_d+1 < len(T)):
      ind_d += 1
      sum += T[ind_d]
    while (ind_g-1 >= 0):
      ind_g -= 1
      sum += T[ind_g]
  
  rec_g = Method3(T[:m])
  rec_d = Method3(T[m:])
  
  return Maximum_tuple_first_element((sum, ind_g,ind_d), 
  (rec_g[0], rec_g[1], rec_g[2]),
  (rec_d[0], rec_d[1] + m, rec_d[2] + m))


#______________TEST_____________

chosenList = [-2,-1,0,1,2]
print("T =", chosenList)
print("S =", (Method3(chosenList)[1], Method3(chosenList)[2]), "et la somme est de " , Method3(chosenList)[0])

#Generate 1 random numbers between -10 and 10
randomlist = random.sample(range(-10,10), 1)
print("T =", randomlist)
print("S =", (Method3(randomlist)[1], Method3(randomlist)[2]), "et la somme est de " , Method3(randomlist)[0])

#Generate 5 random numbers between -10 and 0
randomlist = random.sample(range(-10,0), 5)
print("T =", randomlist)
print("S =", (Method3(randomlist)[1], Method3(randomlist)[2]), "et la somme est de " , Method3(randomlist)[0])

#Generate 10 random numbers between -10 and 10
randomlist = random.sample(range(-10,10), 10)
print("T =", randomlist)
print("S =", (Method3(randomlist)[1], Method3(randomlist)[2]), "et la somme est de " , Method3(randomlist)[0])

#Generate 20 random numbers between -100 and 100
randomlist = random.sample(range(-100,100), 20)
print("T =", randomlist)
print("S =", (Method3(randomlist)[1], Method3(randomlist)[2]), "et la somme est de " , Method3(randomlist)[0])