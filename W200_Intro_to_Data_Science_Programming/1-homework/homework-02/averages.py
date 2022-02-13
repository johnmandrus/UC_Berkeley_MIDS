a = float(input("Enter a number: "))
b = float(input("Enter another number: "))
avg_type = int(input("Choose an average type: "))
if avg_type == 1:
    print((a+b)/2)
elif avg_type == 2:
    print((a+b)**0.5)
elif avg_type == 3:
    print(((a**2+b**2)/2)**0.5)
else:
    print("Invalid input. Why can't you just follow simple instructions??")