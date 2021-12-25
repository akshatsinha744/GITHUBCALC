import math
a = float(input("ENTER NUM1:\n"))
b = float(input("ENTER NUM2:\n"))
print("choose the desired operation\n 1.ADDITION(A)\n2.SUBTRACTION(S)\n3.MULTIPLICATION(M)\n4.DIVISION(D)")

c = input()
if(c == "A"):
    print(a+b)
    
elif(c == "S"):
    print(a-b)
    
elif(c == "M"):
    print(a*b)
    
elif(c == "D"):
    print(a/b)

print("DID YOU WANT TO DO SOME TRIGONOMETRIC CALCULATION\n")
    
d = float(input("ENTER THE ANGLE VALUE ON RADIAN\n"))

print("1.SIN(s)\n2.COS(c)\n3.TAN(t)\n,4.COSEC(co)\n.5.COT(ct)\n.6.SEC(se)")


f = input()

if(f == "s"):
    print(math.sin(int(d)))
elif(f == "c"):
    print(math.cos(int(d)))
elif(f == "t"):
    print(math.tan(int(d)))
