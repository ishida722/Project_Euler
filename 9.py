def IsPythagorean(a, b, c):
    if (a*a) + (b*b) == (c*c):
        return True
    else:
        return False

rng = range(1, 999)

for a in rng:
    for b in rng:
        c = 1000 - a - b
        if c <= 0:
            break
        if IsPythagorean(a, b, c):
            print('{0},{1},{2}:{3}'.format(a, b, c, a*b*c))
