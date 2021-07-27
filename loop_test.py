from time import perf_counter

start = perf_counter()
sum = 0
for i in range(10000):
    for j in range(10000):
       sum += i*j
end = perf_counter()

print(end-start)
