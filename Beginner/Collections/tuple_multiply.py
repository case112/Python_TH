def multiply(*args):
    product = 1
    for arg in args:
        product *= arg
    return product


print(multiply(5,6,4,2,3,4,5,6))