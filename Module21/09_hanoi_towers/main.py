def hanoi(N, i, k): # N - всего, i - с какого стержня, k - на какой стержень
    if N == 1:
        print("Переложить диск 1 со стержня номер {} на стержень номер {}".format(i, k))
        return 1
    else:
        temp = 6 - i - k
        hanoi(N - 1, i, temp)
        print("Переложить диск {} со стержня номер {} на стержень номер {}".format(N, i, k))
        hanoi(N - 1, temp, k)


N = int(input("Введите кол-во дисков: "))
hanoi(N, 1, 3)
