fibo = [1,2]
fibo_gu = 2

while fibo[-1] <= 4000000:
    fibo_end = fibo[-1]+fibo[-2]
    if fibo_end % 2 == 0:
        fibo_gu += fibo_end
    fibo.append(fibo_end)

print(fibo_gu)

