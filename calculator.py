a = int(input("Enter the first number："))
b = int(input("Enter the second number："))
if b == 0:
        print("Divisor cannot be zero")
        exit(-1)
sign = input("Enter calculation method  ：(+-*/)")
if sign == "+":
    print("%s%s%s=%s"%(a,sign,b,a+b))
elif sign == "-":
    print("%s%s%s=%s"%(a,sign,b,a-b))
elif sign == "*":
    print("%s%s%s=%s"%(a,sign,b,a*b))
elif sign == "/":
   print("%s%s%s=%s"%(a,sign,b,a/b))