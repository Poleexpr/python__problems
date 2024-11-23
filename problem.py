
arr = input('input 10 integers pls ')
l = list(map(int, arr.split(' ')))
filtred_l = filter(lambda x: x % 2 != 0, l)
filtred_list = list(filtred_l)

if len(filtred_list) == 0:
  print('no')
else:
  filtred_list.sort(reverse=True)
  print(filtred_list[0])
  




