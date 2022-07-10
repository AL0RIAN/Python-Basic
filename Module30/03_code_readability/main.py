from typing import List

print("Вариант 1")
result1: List[int] = [x for x in range(2, 1001)]
for i in range(2, 100):
    result1 = list(filter(lambda x: x == i or x % i, result1))
print(result1)

print("\nВариант 2")
numbers = range(2, 1000)
result2: List[int] = []

for number in numbers:
    border = number ** 1 // 2
    flag = True
    for i in range(2, border + 1):
        if number % i == 0:
            flag = False
            break

    if flag:
        result2.append(number)

print(result2)

