numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
characters = ["!", "@", "#", "$", "%", "&", "?"]
password = input("Create your password(min 8characters): ")

if len(password) < 8:
    print("Your password should have a minimun of 8 characters. Try again.")
elif not any(char in password for char in characters):
    print("Your password should include at least a special character")
else:
    if not any(num in password for num in numbers):
        print("Your password should contain at least 1 digit")
    else:
        print("Your password is strong enough")