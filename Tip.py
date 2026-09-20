def total_calc(amt,tip):
    
    total = amt + tip
    total = round(total,2)
    return total

print("Total Money paid: ₹",total_calc(55.689,25.106))
    