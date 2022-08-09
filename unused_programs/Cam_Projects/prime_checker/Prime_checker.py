def bazooka(num):
    for i in range(2, num):
        if num%i == 0:
            return "Your number is not prime :/ \nIt is divisible by " + str(i)

    return "Your number is prime :)"


user = int(input("Input a number "))
print(bazooka(user))
