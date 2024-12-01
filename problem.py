def sum(arr):
    if(len(arr) == 0):
        return 0
    elif(len(arr) == 1):
        return arr[0]
    else:
        return arr[0] + sum(arr[1:])



def length_arr(arr, k):
    if(len(arr) == 0):
        return k
    else: 
        return length_arr(arr[1:], k + 1)


m = 0

def max(arr):
    if(type(arr) == int):
        return arr
    else:
        if(arr[0] > arr[1]):
            return max(arr.pop(0))
        else:
            return max(arr.pop(1))

print(max([1, 2, 3, 4]))

def max2(list):
   if len(list) == 2:
    return list[0] if list[0] > list[1] else list[1]
   sub_max = max(list[1:])
   return list[0] if list[0] > sub_max else sub_max



  




