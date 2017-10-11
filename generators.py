############ ez nem mukodik ####################
amount = 1000
new_amount = 0

def min_period(a):
    percent = (a+100) / 100
    while new_amount < amount * 2:
        yield amount
        amount = amount * percent



b = min_period(3)
count = 0
for i in b:
    count += 1

print(count)

############ ez mukodik ####################
"""
def whatever(interest, amount, aim):  
    count = 1
    while (aim > amount):
        amount = amount * ((interest+100) / 100)   
        count += 1
    print(count)


whatever(3, 1000, 2000)
"""
