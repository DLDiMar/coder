def fizz_buzz(input):
    if(input % 3 == 0 and input % 5 == 0):
        return 'Fizz Buzz'
    elif(input % 3 == 0):
        return 'Fizz'
    elif(input % 5 == 0):
        return 'Buzz'
    else:
        return input


print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(7))
print(fizz_buzz(15))