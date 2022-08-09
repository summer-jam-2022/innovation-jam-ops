num = (input("Give me a positive integer "))
while not num.isnumeric():
    num = (input("Try again and give me a positive integer idiot "))
num = int(num)    
while num > 1:
    if num%2 == 1:
        num = ((3 * num) + 1)
    elif num%2 == 0:
        num = (num/2)
    print(num)
