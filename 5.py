def validate_div(target):
    for val in range(1, 21):
        if target % val != 0:
            return False
    return True

def search_div_number():
    val = 20
    while 1:
        if validate_div(val):
            return val
        val = val + 20


print(validate_div(2520))
print(search_div_number())
