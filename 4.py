import itertools

def valdate_palindromic(num):
    str_num = str(num)
    len_num = len(str_num)
    if len_num % 2 != 0:
        return False
    for val in range(0, int(len_num/2)):
        if str_num[val] != str_num[-val-1]:
            return False
    return True

def palindromic(num_list):
    pal_list = []
    calc_list = list(itertools.product(num_list, num_list))
    for val in calc_list:
        pal = val[0] * val[1]
        if valdate_palindromic(pal):
            pal_list.append(pal)
    return pal_list

keta2 = list(range(10,100))
keta3 = list(range(100,1000))

print(max(palindromic(keta3)))
