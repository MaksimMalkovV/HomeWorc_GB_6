from random import randint as rand
import math
data = [rand(5,25) for i in range(10)]
print(f"Исходный список {data}")
res = list([a*b for a,b in zip(data[0:math.ceil(len(data)/2)],data[::-1])])
print(f"Результат: {res}")