## Functions in Python

def user_welcome():
    print("Hello user, welcome to functions in Python")

user_welcome()

def user_stats(name, age, birthday): ## 3 Parameters
    print("Hello " + name + ", you are " + str(age) + " years old, meaning you were born in " + birthday)

user_stats("Mandy", 70, "19/09/1999") ## Parameters passed as their respective data types

def cube(num):
    return pow(num, num)

print(cube(3)) ## Parameter 'num' is passed as an integer

def power_of_num(num1, num2):
    return pow(num1, num2)

result = power_of_num(4, 2)
print(result)

print("Another way of printing power_of_num function: " + str(power_of_num(3, 2)))

## Actual way without having to convert the function into a string
print(power_of_num(3, 2))