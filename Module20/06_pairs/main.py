import random

original_list = [random.randint(1, 100) for _ in range(10)]
new_list = [(original_list[number], original_list[number + 1]) for number in range(0, 9, 2)]
print(original_list)
print(new_list)
