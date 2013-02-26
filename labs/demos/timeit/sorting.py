import timeit
repeats = 1000
for f in ('selectionSort', 'insertionSort', 'bubbleSort'):
    t = timeit.Timer('{0}([10, 9, 1, 2, 5, 3, 8, 7])'.format(f),
        'from sorting import selectionSort, insertionSort, bubbleSort')
    sec = t.timeit(repeats) / repeats
    print '{f}\t{sec:.6f} sec'.format(**locals())