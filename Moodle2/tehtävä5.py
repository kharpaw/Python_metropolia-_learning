talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))


talents_to_pounds = talents * 20
total_pounds = talents_to_pounds + pounds

pounds_to_lots = total_pounds * 32
total_lots = pounds_to_lots + lots

total_grams = total_lots * 13.3

kilograms = int(total_grams / 1000)
grams = total_grams % 10000

print("\nThe weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")