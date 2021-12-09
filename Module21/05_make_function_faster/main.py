def calculating_math_func(data, cache={}):
    if data in cache.keys():
        result = cache[data]
    else:
        result = 1
        for index in range(1, data + 1):
            result *= index
        cache[data] = result
    result /= data ** 3
    result = result ** 10
    return result

print(calculating_math_func(5))
print(calculating_math_func(5))
