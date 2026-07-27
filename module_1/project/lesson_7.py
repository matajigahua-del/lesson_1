
bill_amount=float(input("Enter the amount of bill ($) - "))
bill_paid=float(input("Enter the amount paid by the customer (in dollars) - "))
shop_return=bill_paid-bill_amount
if shop_return>0:
    print("The shopkeeper has to return the amount to the customer")
else:
    print("The shop_return is paid")