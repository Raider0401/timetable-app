#import password module

adminRecord=[]
teacherRecord=[]
studentRecord=[]

def newTeacher(record):
    teacherName=input("Please enter the teacher's name: ")
    username=input("Please enter the teacher's username: ")
    password="123" #fucntion- password()
    teacherID=len(record)+1
    record.append([teacherID, teacherName, username, password])

#newstudent
#update
#approve password
#make time table