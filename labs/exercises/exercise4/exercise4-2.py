# First, let's try generating all triangles with sides equal to or smaller than 10.
# print [(a,b,c) for c in range(1, 11) for b in range(1, 11) for a in range(1, 11)]

# Next, we'll add a condition that they all have to be right triangles. We'll also modify this function by taking into consideration that side b isn't larger than the hypothenuse and that side a isn't larger than side b.
# print [(a,b,c) for c in range(1, 11) for b in range(1, c + 1) for a in range(1, b + 1) if a ** 2 + b ** 2 == c ** 2]

# Finally, we just modify the function by saying that we want the ones where the perimeter is 24.
# print [(a,b,c) for c in range(1, 11) for b in range(1, c + 1) for a in range(1, b + 1) if a ** 2 + b ** 2 == c ** 2 and a + b + c == 24]