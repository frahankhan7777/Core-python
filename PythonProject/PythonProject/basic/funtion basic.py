def calculation (num1, num2):
    add = (num1 + num2)
    min = (num1 - num2)
    mul = (num1 * num2)
    div  = (num1 / num2)
    return add, min, mul, div


a, b, c, d, = calculation(2, 1)
print("addition is", a)
print("addition is", b)
print("addition is", c)
print("addition is", d)


