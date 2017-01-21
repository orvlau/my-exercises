totalprice = []
price = []

while (price!=0):
	price = input("Please enter price: ")
	totalprice.append(price)
	print sum(totalprice)
else:
	print "Total price is: ", sum(totalprice)
	cash = input("Please enter cash: ")
	print "Your change is: ", (cash - sum(totalprice))

