def SumOfSquare(num):
    ret = 0
    for val in range(1, num+1):
        ret += val*val
    return ret

def SquareOfSum(num):
    ret = 0
    for val in range(1, num+1):
        ret += val
    return ret*ret

num = 100
sq = SquareOfSum(num)
su = SumOfSquare(num)
print(sq)
print(su)
print(sq-su)
