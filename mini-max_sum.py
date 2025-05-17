import math
values = arr #We have access to "n" in the problem
results = list()
max_value = 0
min_value = 0

for i in range(len(values)):
    res = sum(values[:i] + values[i+1:])
    results.append(res)

cont = 0
for value in results:
    if cont == 0:
        min_value = value
        max_value = value
    if value > max_value:
        max_value = value
    if value < min_value:
        min_value = value
    cont += 1

print(max_value, min_value)