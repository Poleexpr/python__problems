from time import perf_counter
import threading

def f(x):
    return pow(x, 2) - pow(x, 2)+ (x * 4) - (x * 5) + x + x

def f2(x):
    return x + x

def f3(x):
    return f(x) + f2(x)

threads = []
for n in range(0, 10000):
    t = threading.Thread(target=f, args = {n})
    t2 = threading.Thread(target=f2, args = {n})
    threads.append(t)
    threads.append(t2)
    t.start()
    t2.start()       

for t in threads:
    t.join()

end_time = perf_counter()

print(f'Выполнение заняло {end_time} секунд.')


threads3 = []
for n3 in range(0, 10000):
    t3 = threading.Thread(target=f3, args = {n})
    threads.append(t3)
    t3.start()
        

for t3 in threads3:
    t3.join()

end_time3 = perf_counter()

print(f'Выполнение заняло {end_time3} секунд.')





