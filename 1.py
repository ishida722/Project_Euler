three = []
five = []
answer = 0

for var in range(1,1000):
    if var%3 == 0:
        three.append(var)
    elif var%5 == 0:
        five.append(var)
print(three)
print(five)

for var in three:
    answer += var

for var in five:
    answer += var

print(answer)
