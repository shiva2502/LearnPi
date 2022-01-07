p = input()
m = input()

p1 = p[0]
p2 = p[1]
ap = p1+p2
ap = int(ap)

if (ap >= 75):
    print("Allowed to write exam")
elif (ap < 75 and m =="Y"):
    print("Allowed to write exam")
elif (ap < 75 and m =="N"):    
    print("Cannot write exam")
else:
    print("Invalid input")

print("Pull added")
print("Pull added2")
Print("Branch")