a=int(input("enter the number"))
for i in range(2,a):
    if a%i==0:
        chk=True
        break

    else:
        chk=False
if chk:
    print("not a prime number")
else:
    print("it is a prime number")