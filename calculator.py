def calc(a, b):
    sum = a + b
    
    sub = a - b
 
    mul = a * b
  
    div = a / b

    arr = [sum, sub, mul, div]
  
    for x in range(len(arr)):
        print (arr[x]),
a = int(input("Enter first number："))
b = int(input("Enter second number："))
calc(a, b)