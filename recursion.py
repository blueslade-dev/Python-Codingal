def factorial(num):
    '''A docstring of the function'''
    if num == 0  or num == 1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial.__doc__)

print(factorial(1))
print(factorial(5))
print(factorial(3))
print(factorial(8))
print(factorial(6))