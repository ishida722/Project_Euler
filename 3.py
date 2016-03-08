prime_list = [2]

def next_prime(now_prime):
    prime = now_prime + 1
    for val in prime_list:
        if prime % val == 0:
            prime = next_prime(prime)
    return prime

def make_prime_list(max_num):
    while prime_list[-1] <= max_num:
        prime_list.append(next_prime(prime_list[-1]))

def prime_fact(num):
    fact_list = []
    while 1:
        while num % prime_list[-1] == 0:
            num /= prime_list[-1]
            fact_list.append(prime_list[-1])
        prime_list.append(next_prime(prime_list[-1]))
        if num == 1:
            break
    return fact_list

print(prime_fact(600851475143))

# while 1:
#     if n % i == 0:
#         n /= i
#     else:
#         i += 1
#         for var in prime_list:
#             i % var == 0
