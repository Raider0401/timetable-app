database={}

#Deployed when a user signs up
def sign_up(database):
    username=input("Please enter your username: ")
    password=input("Please enter your password: ")
    re=""
    while re!=password:
        re=input("Please re-enter the same password: ")
    schl_name=input("Please enter the name of the school: ")
    prin_name=input("Please enter the name of the principal: ")
    database[username]=password

#Deployed when a user logs in
def login(username):
    usinp=input("Please enter your username: ")
    if usinp in database.keys:
        psinp=input("Please enter your password: ")
    else:
        print("Username not found!")
    if psinp==database[username]:
        print("Login successful!")

sign_up()