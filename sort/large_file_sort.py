import random
from itertools import zip_longest


def generateRandomNumbers():
    file = open('random.txt', 'w')
    for val in range(1000000):
        line = str(random.randint(1, 99)) + '\n'
        file.writelines(line)
    file.close()
    print('Random numbers generated!')


def mergeAndSort(alist):
    print("Splitting ", alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeAndSort(lefthalf)
        mergeAndSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
    print("Merging ", alist)
    return alist


def grouper(n, iterable, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(fillvalue=fillvalue, *args)


def fileSort(chunk):
    with open('random.txt') as f:
        for i, g in enumerate(grouper(N, f.read().splitlines(), fillvalue=''), 1):
            with open('chunk_{0}'.format(i * N), 'w') as fout:
                sorted_val = mergeAndSort(list(map(int, g)))
                #print(i * N)
                fout.writelines('\n'.join(list(map(str, sorted_val))))

N = 1000
fileSort(N)
#generateRandomNumbers()
