with open("commonpsswd.txt", "r") as fh:
    commonPasswords=fh.read().splitlines()

passApprove=False
while passApprove==False:
    password=input("Please enter your password: ")
    if password in commonPasswords:
        print("Password is too common, please enter a different one!")
        continue
    elif len(password)<10:
        print("Password shorter than 10 characters, please try again!")
        continue
    elif len(password)>30:
        print("Password longer than 30 characters, please try again!")
        continue
    splCharacter=False
    upperCharacter=False
    numCharacter=False
    for character in password:
        if character.isspace==False and character.isalnum==False:
            splCharacter=True
        elif character.isalpha()==True and character.isupper()==True:
            upperCharacter=True
        elif character.isnumeric()==True:
            numCharacter=True
    if splCharacter==False:
        print("Please include a special character in your password to make it strong!")
        continue
    elif upperCharacter==False:
        print("Please include an upper case character in your password!")
        continue
    elif numCharacter==False:
        print("Please include a number in your password!")
        continue

    passApprove=True