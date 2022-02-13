fuel_gal = float(input("Enter volume of gasoline in gallons: "))
fuel_l = fuel_gal*3.7854
fuel_b = fuel_gal/19.5
fuel_price = fuel_gal*3.65
print("Volume of gasoline in liters is","{:.4f}".format(fuel_l))
print("Volume of gasoline in barrels is","{:.3f}".format(fuel_b))
print("Price of gasoline in USD is $","{:.2f}".format(fuel_price))