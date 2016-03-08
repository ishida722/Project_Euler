prime_list = [2, 3]

def IsPrime(num):
    isPrime = True
    for i in prime_list:
        if i*i  > num:
            break
        if num % i == 0:
            isPrime = False
            break
    if isPrime:
        prime_list.append(num)
    return isPrime

def make_prime_list(maxNum):
    num = 3
    while num <= maxNum:
        num = num + 2
        IsPrime(num)

# make_prime_list(10000)
make_prime_list(2000000)
print(sum(prime_list))
