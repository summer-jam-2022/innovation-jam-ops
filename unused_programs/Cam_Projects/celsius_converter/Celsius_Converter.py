def C2F(degrees_C):
    degrees_F = (9/5 * degrees_C + 32)
    return degrees_F

def F2C(degrees_F):
    degrees_C = (5/9 * (degrees_F - 32))
    return degrees_C


user = float(input("Give me a number in celsius! "))
prime = C2F(user)
print(str(prime) + " degrees fahrenheit")
