'''
Write a program that asks the user for a username and password.
If either or both are incorrect, the program ask the user to enter the username and password again.
This continues until the login information is correct or wrong credentials have been entered five times.
If the information is correct, the program prints out Welcome.
After five failed attempts the program prints out Access denied. The correct username is python and password rules.
'''

username = "pawan"
password = "Metropolia"
attempts = 0
max_attempts = 5


while True:
    user = input("Enter you username: ")
    pass_word = input("Enter you password: ")
    
    if user == username and pass_word == password:
        print("You are welcome")
        break
    
    else:
        attempts += 1
        if attempts == max_attempts:
            print("Access denied")
        
        else:
            print("Incorrect. Try again")