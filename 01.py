import numpy as np
price = np.array([100,200,300])
quantity = np.array([2,3,1])
total = sum(price*quantity)
print("Total cost = ",total)
discount = 10
tax = 5
discount_amt = (discount/100)*total
after_discount = total - discount_amt
print("After discount the total cost = ",after_discount)
tax_amt = (tax/100)*after_discount
print("Tax amount = ",tax_amt)
final_cost = tax_amt + after_discount
print("Final cost = ",final_cost)


