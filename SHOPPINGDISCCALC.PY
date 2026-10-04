
print("==SHOPPING BILL PAYMENT PLAN==")
while True:
   try:
      people = int(input("Enter the number of people:")) 
      bill_amt = float(input("Enter the bill you have to pay: ₹"))
      bill_amt = round(bill_amt, 2)
      if people <= 0:
         print("There cannot be zero or negative no.of people.")
         continue
      
   except ValueError as ex:
      print("Exception: ",ex,"\nTry again.")
      continue
   else:
      print("Okay")
      break
   finally:
      print("Processing........")


def calculatebill(discount_percentage,mrp):
   discount_amt = discount_percentage/100 * mrp
   bill = mrp - discount_amt
   return bill

checking = True
while checking:
   try:
      dpercent = int(input("Enter the discount percentage: "))
      if 0 > dpercent:
         print(f"D{"%"} can't be negative ")
         continue
      elif 100 < dpercent:
         print(f"D{"%"} can't be greater than 100 ")
         continue
   except ValueError:
      print("Exception: ", ex) # ex = ValueError as assigned earlier in the code 
      continue   
   else:
      break 

   
bill = calculatebill(dpercent, bill_amt)

bill_per_person = bill/people

print("Final Bill after Discount: ₹",round(bill, 2))
print("Each person pays: ₹",round(bill_per_person , 2))
print("====================================")