import cProfile
import sorting
import random
l = range(500)
random.shuffle(l)
cProfile.run('sorting.selectionSort(l)')
