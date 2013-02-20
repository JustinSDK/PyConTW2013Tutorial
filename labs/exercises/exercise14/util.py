def ascending(a, b): return a - b
def descending(a, b): return -ascending(a, b)
# selection sort
def sorted(xs, compare = ascending):
    return [] if not xs else __select(xs, compare)

def __select(xs, compare):
    selected = reduce(
        lambda slt, elem: elem if compare(elem, slt) < 0 else slt, xs)
    remain = [elem for elem in xs if elem != selected]
    return (xs if not remain
               else [elem for elem in xs if elem == selected] 
                   + __select(remain, compare))

print sorted([2, 1, 3, 6, 5])
print sorted([2, 1, 3, 6, 5], descending)