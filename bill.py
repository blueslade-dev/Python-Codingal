def total_bill(bill_amt, tip_perc):
    bill = bill_amt + ((tip_perc/100) * bill_amt)
    return bill

print("Bill: ",total_bill(300,15))

def seating_arrangement(guests):

    '''Find the number of seating of the guests'''
    if guests == 0 or guests == 1:
        return 1

    else:
        return guests * seating_arrangement(guests-1)

print(seating_arrangement.__doc__)

i = 1
while i <= 10:
    if i == 1:
      print(f"\nSeating arrangement for {i} guest",seating_arrangement(i))
    else:
        print(f"\nSeating arrangement for {i} guests",seating_arrangement(i))
    i += 1

