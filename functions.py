def calculate_discount(price,discount_percent):
   if discount_percent >= 20:
      discounted_price= price-(price*(discount_percent/100))

      return discounted_price
   else:
      return price
   
original_price=input("Enter the original_price")
discount_percent=input("Enter the dicount percentage")

final_price= calculate_discount(original_price,discount_percent)

if final_price!= original_price:

 print("Final price after discount:",final_price)

else:

 print("No discount.Final price:",final_price)