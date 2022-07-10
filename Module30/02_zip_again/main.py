from typing import List

if __name__ == "__main__":
    count = int(input("Введите кол-во элементов (N): "))

    # letters: List[str] = ['a', 'b', 'c', 'd', 'e']
    # numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

    letters: List[str] = [input(f"Введите {elem + 1} букву: ") for elem in range(count)]
    print()
    numbers: List[int] = [int(input(f"Введите {elem + 1} число: ")) for elem in range(count)]

    result = list(map(lambda x, y: (x, y), letters, numbers))
    print("\n", result)

