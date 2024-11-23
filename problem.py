def f(x, y, z):
  
  list1 = []
  if x %2 == 0:
    list1.append(x)
  if y %2 == 0:
    list1.append(y)
  if z %2 == 0:
    list1.append(z)

  if len(list1) > 0: 
    list1.sort(reverse = True)
    return list1[0]
  else:
    return 'no'

 
  
  

    
print(f(1, 1, 1))




