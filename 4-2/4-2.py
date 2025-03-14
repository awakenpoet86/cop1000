name = input("Employee's name: ")
shift = int(input("Number of Shifts: "))
transactions = int(input("Number of Transactions: "))
tvalue = float(input("Transaction dollar value: "))

score = int((tvalue/transactions)/shift)

if score <=30: 
    bonus = 50
elif score >=31 and score <=69:
    bonus = 75
elif score >=70 and score <=199:
    bonus = 100
else: 
    bonus = 200

print("Employee's name: "+name)
print("Employee's bonus:",bonus)