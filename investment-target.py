#!/usr/bin/python

initial_deposit = input("Initial Investment($) : ")
return_rate = input("Return Rate(%) : ")
timeline = input("Target Time (in month): ")

return_amount = 0
total_month = initial_deposit + return_amount

for i in range (1,timeline+1):
	return_amount = (return_rate/100.0) * total_month
	total_month += return_amount
	print "#" + str(i) + ":" + str(total_month)



