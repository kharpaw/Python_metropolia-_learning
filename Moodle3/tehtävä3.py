'''
Write a program that asks for the biological gender and hemoglobin value (g/l).
The program the notifies the user if the hemoglobin value is low, normal or high.

A normal hemoglobin value for adult females is between 117-155 g/l.
A normal hemoglobin value for adult males is between 134-167 g/l.
'''


gender = input("Enter the biological gender (female/male): ")
hemoglobin_value = int(input("Enter the hemoglobin value (g/l): "))

if gender == "female":
    if hemoglobin_value < 117:
        print("Hemoglobin value is low.")
    elif hemoglobin_value <= 155:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")
elif gender == "male":
    if hemoglobin_value < 134:
        print("Hemoglobin value is low.")
    elif hemoglobin_value <= 167:
        print("Hemoglobin value is normal.")
    else:
        print("Hemoglobin value is high.")
else:
    print("Invalid gender entered.")