from classes import Customer, LoyalCustomer, Flat, RealEstateCompany


customer_1 = Customer("r@s.lt", "Rokas")
print(customer_1.total_amount(200))
customer_2 = Customer("a@b.com", "Nerokas")
print(customer_2.total_amount(500))
customer_3 = Customer("c@d.eu", "Demi")
customer_3_total_amount = customer_3.total_amount(200)

loyal_customer_1 = LoyalCustomer("c@d.eu", "Demi")
print(loyal_customer_1.total_amount(100000))
loyal_customer_2 = LoyalCustomer("a@b.lt", "Rokas")
print(loyal_customer_2.total_amount(2500000))
loyal_customer_3 = LoyalCustomer("c@d.eu", "Demi")
loyal_customer_3.total_amount(300)
print(loyal_customer_3)

flat1 = Flat(500, "antakalnio")
flat2 = Flat(200, "Zirmunu")

res1 = RealEstateCompany([customer_1, customer_2, customer_3, loyal_customer_3], [flat1, flat2])
res1.sell(res1.cheapest(), customer_2)

res1.sell(res1.cheapest(), loyal_customer_3)
