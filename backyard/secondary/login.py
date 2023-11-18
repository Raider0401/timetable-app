#make a radio button choice for this
 
adminUserData={"admin@school.com":"1234"}
teacherUserData={"teacher@school.com":"1234"}
studentUserData={"student@school.com":"1234"}
 
loginProcess=True
while loginProcess==True:
    loginMode=input("Please enter how you want to log in (admin/teacher/student): ")
    if loginMode=="admin":
        userData=adminUserData
    elif loginMode=="teahcer":
        userData=teacherUserData
    elif loginMode=="admin":
        userData=studentUserData
    #else
    #Put in code for exception handling
 
    username=input("Please enter your username:")
    if username in userData.keys():
        password=input("Please enter your password: ")
        if userData[username]==password:
            print("Login Successful!")
            loginProcess=False
        #else:
 
 
#password entry error
 
#with and without colour options
#use pandas
 
#requests to change passwords
