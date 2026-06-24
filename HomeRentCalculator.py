"""
1). Inputs we need from the user.
2). Total rent.
3). Total food expense (sankes Included).
4). Electricity Units spends.
5.) per unit charges.
6). Person Living in PG-Flat.
-> Output section
1). The Total amount you will pay.
"""
from binascii import crc_hqx

rent = int(input("Enter your PG/Flat rent = "))
food = int(input("Enter the amount of total food expense(Included sankes) = "))
electricity_spend = int(input("Enter the total of elecritcity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
person = int(input("Enter the total person living in one flat = "))

total_bill = electricity_spend *charge_per_unit
total = (rent + food + total_bill) // person
print("Each person will pay = ", total)