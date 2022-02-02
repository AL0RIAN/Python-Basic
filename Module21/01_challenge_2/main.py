def counter(number, count=1):
    if count == number:
        return count
    else:
        print(count)
        return counter(number, count + 1)


num = int(input("Enter num: "))
print(counter(num))
