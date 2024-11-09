print("write all your marks out of 100")

m1 = int(input("mark 1"))
m2 = int(input("mark 2"))
m3 = int(input("mark 3"))
m4 = int(input("mark 4"))
m5 = int(input("mark 5"))

avg = m1+m2+m3+m4+m5//5

if avg>=91:

    print("A1+")

elif avg>=81:

    print("A1")

elif avg>=71:

    print("A2")

elif avg>=61:

    print("B")

elif avg>=51:

    print("C")

elif avg<=50:

    print("FAIL")

else:

    print("INVALID INPUT!")