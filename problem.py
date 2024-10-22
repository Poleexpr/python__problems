def broke_chocolate(n, m, countN=0, countM=0):
  if(n == 1 and m == 1):
    return countN + (countM * (countN + 1))
  elif(n == 1 and m > 1):
    return broke_chocolate(n, m-1, countN, countM+1)
  else:
    return broke_chocolate(n-1, m, countN+1, countM)

print(broke_chocolate(1, 1))


