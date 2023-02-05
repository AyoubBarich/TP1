def Maximum_tuple_first_element(T1, T2, T3):
  sum_max = max(T1[0],T2[0],T3[0])
  if (T1[0] == sum_max):
    return T1
  elif (T2[0] == sum_max):
    return T2
  else :
    return T3

def Methode3_rec(T, d, f):
  if (d == f):
    return (T[d], d, f)
  
  if (f - d == 1):
    if (T[d] > 0 and T[f] > 0 ):
      return (T[d]+T[f],d ,f)
    elif (T[d] > 0):
      return (T[d], d, d)
    elif (T[f] > 0):
      return (T[f], f, f)
    elif (T[d] > T[f]):
      return (T[d], d, d)
    else:
      return (T[f], f, f)

  
  m = (d + f) // 2
  sum_temp = T[m]
  sum_max = sum_temp

  T_gauche = Methode3_rec(T, d, m-1)
  T_droite = Methode3_rec(T, m+1, f)


  sum_d = T[m]  
  sum_d_max = sum_d
  d_max = m 

  for ind_d in range (m - 1, d - 1, -1):
    sum_d += T[ind_d]
    if (sum_d_max <= sum_d):
      sum_d_max = sum_d
      d_max = ind_d

  sum_f = T[m]  
  sum_f_max = sum_f
  f_max = m 

  for ind_f in range (m + 1, f + 1):
    sum_f += T[ind_f]
    if (sum_f_max <= sum_f):
      sum_f_max = sum_f
      f_max = ind_f

  sum_max = sum_d_max + sum_f_max - T[m]

  return Maximum_tuple_first_element((sum_max,d_max,f_max), T_gauche, T_droite)

def Methode3(T):
  return Methode3_rec(T,0,len(T)-1)


print(Methode3([-10, 10, 10, -3, 3]))