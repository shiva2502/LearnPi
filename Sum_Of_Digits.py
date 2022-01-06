n = input()

nlen = len(n)


if nlen==1:
   n0 =int(n[0])
   print(n0)
elif nlen==2:
    n0 =int(n[0])
    n1 =int(n[1])
    print(n0+n1)
elif nlen==3:
    n0 =int(n[0])
    n1 =int(n[1])
    n2 =int(n[2])
    print(n0+n1+n2)
elif nlen==4:
    n0 =int(n[0])
    n1 =int(n[1])
    n2 =int(n[2])
    n3 =int(n[3])
    print(n0+n1+n2+n3)
else:
    print("Invalid Range")

print("Pull added")