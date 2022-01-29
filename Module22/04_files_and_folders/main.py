import os


def size_dir(directory, cache):
    if os.path.isfile(directory):
        cache['files'] += 1
        cache['size'] += os.path.getsize(directory)
        return 1
    else:
        cache['dirs'] += 1
    for elem in os.listdir(directory):
        size_dir(os.path.abspath(os.path.join(directory, elem)), cache)
    return 1


path = os.path.abspath("..")
result = {'size': 0, 'files': 0, 'dirs': 0}
size_dir(path, result)
print("Размер каталога (в Кб):", result['size'] * 0.001)
print("Количество подкаталогов:", result['dirs'])
print("Количество файлов:", result['files'])
