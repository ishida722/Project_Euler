prime_list = [2]

def next_prime(now_prime):
    prime = now_prime + 1
    for val in prime_list:
        if prime % val == 0:
            prime = next_prime(prime)
    return prime

def make_prime_list(max_len):
    while len(prime_list) < max_len:
        prime_list.append(next_prime(prime_list[-1]))

make_prime_list(10001)
print(prime_list)
