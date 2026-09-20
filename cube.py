def cube(num):
    cube = num ** 3
    return cube

def by_three(num):
    if num % 3 == 0:
        return cube(num)
    else:
        return False

print(by_three(16))
print(by_three(9))  