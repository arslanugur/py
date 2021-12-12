# Monthly Bills

# Payday Start Money

pay = 1000

#Bills for the house
rent = 200
gas_elec = 80
council_tax = 100
water = 30

# Total of the house bills
total_house = rent + gas_elec + council_tax + water


# General Outgoings
bike = 30
phone = 20 
spotify = 10

# Total of the general bills
total_general = bike + phone + spotify

# Temporary bills
owed_friend = 20

# Total of the temporary bills
total_temp = owed_friend

# Total outgoings
total_outgoing = total_house + total_general + total_temp


# Pay after bills
pay_after = pay - total_outgoing

print ("THIS MONTHS BILLS")
print ("House Bills:",round (total_house, 2))
print ("General Bills:",round(total_general, 2))
print ("Temporary:",round(total_temp,2))
print ("Total Outgoings", round(total_outgoing, 2))
print ("Pay:", pay)
print ("Pay after bills:", round(pay_after,2))

