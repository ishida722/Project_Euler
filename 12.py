triList = []

def MakeTriangleList(maxNum):
    for num in range(1, maxNum+1):
        tri = int(num*(num+1)*0.5)
        triList.append(tri)

def NextTrinagle():
    num = len(triList) + 1
    tri = int(num*(num+1)*0.5)
    triList.append(tri)
    return tri

def CalcFactors(num):
    factors = []
    numList = list(range(2, int(num / 2 + 1)))
    facNum = 1
    for i in numList:
        if i % facNum == 0:
            factors.append(facNum)
        facNum += 1
    return factors

while 1:
    if len(CalcFactors(NextTrinagle())) > 100:
        print(triList[-1])
        break
