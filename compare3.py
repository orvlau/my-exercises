a = float(input("Enter first grade: "))
b = float(input("Enter second grade: "))
c = float(input("Enter third grade: "))


if ((a>b) and (a>c)):
	print a
elif ((b>a) and (b>c)):
	print b
elif ((c>a) and (c>b)):
	print c
else
	print ""
