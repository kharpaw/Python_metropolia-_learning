'''
1.Write a program that asks a fisher the length of a zander in centimeters.
If the zander does not fulfill the size limit,
the program instructs to release the fish back into the lake and notifies
the user of how many centimeters below the size limit the caught fish was.
A zander must be 42 centimeters or longer to meet the size limit.

'''

zander = int(input("Enter the length of zander: "))

if zander >= 42:
    print(f"The length of the zander is {zander}cm. You may keep the fish.")
else:
    difference = 42 - zander
    print(f"The length of the zander is {zander}cm.")
    print(f"Please release the fish back into the lake.")
    print(f"It was {difference}cm below the size limit.")
    zander = int(input("Enter the length of zander: "))
    print(f"The length of the zander is {zander}cm. You may keep the fish.")