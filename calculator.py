def calc(a, b):
    sum = a + b
    # print(sum)
    sub = a - b
    # print (sub)
    mul = a * b
    # print(mul)
    div = a / b
    # print (div)
    arr = [sum, sub, mul, div]
    # print(sum)
    # print (sub)
    # print(mul)
    # print (div)
    for x in range(len(arr)):
        print (arr[x]),
a = int(input("Enter first number："))
b = int(input("Enter second number："))
calc(a, b)