t = "true"
count = -1
grsum = 0.0

while (t == "true"):
	grinput = float(input("Enter grade(0 to stop):"))
	grsum += grinput
	count += 1
	if (grinput == 0):
		avg = float((grsum/(count)))
		print "Entered", count, "grades with average of:", avg
		t = "false"

