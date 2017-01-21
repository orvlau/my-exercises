withdraw_amount = input("Please enter the amount you wish to withdraw: ")

bills_1k = (withdraw_amount // 1000)
bills_500 = ((withdraw_amount-(bills_1k*1000))//500)
bills_100 = (((withdraw_amount - (bills_1k*1000)) - (bills_500*500)) // 100)

print "1000 bills:", (bills_1k)
print "500 bills:", (bills_500)
print "100 bills:", (bills_100)

