emptyTimetable=[
    {},
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None]
]

alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

timetables12={}
timetables11={}
timetables10={}
timetables9={}

print("This project generates timetable for classes 9 thru 12")

#Excetion handling if i>26
num12Sec=int(input("Please enter the number of sections in grade 12th: "))
for i in range(num12Sec):
    timetables12[alphabet[i]]=list(emptyTimetable)
print(timetables12)
num11Sec=int(input("Please enter the number of sections in grade 11th: "))
for i in range(num12Sec):
    timetables11[alphabet[i]]=list(emptyTimetable)
num10Sec=int(input("Please enter the number of sections in grade 10th: "))
for i in range(num12Sec):
    timetables10[alphabet[i]]=list(emptyTimetable)
num9Sec=int(input("Please enter the number of sections in grade 9th: "))
for i in range(num12Sec):
    timetables9[alphabet[i]]=list(emptyTimetable)

#accepting subjects per section per grade
for grade in [timetables12,timetables11]:#timetables10, timetables9]:
    if grade==timetables11:
        break
    print("for grade")
    for section in grade:
        print("for section")
        choice="no"
        while choice=="no":
            subject=input("please enter the name of subject: ")
            teacher=input("please name the teacher: ")
            grade[section][0][subject]=teacher
            choice=input("done? yes/no ")
    print(grade)


'''teachers12={}
teachers11={}
teachers10={}
teachers9={}

teachersTimetables={}

for i in ["physics","chemistry","maths","english","optional"]:
    print("for",i,";")
    teachersList=[]
    choice="no"
    while choice=="no":
        teacher=input("Please enter the name of the teacher: ")
        teachersList.append(teacher)
        teachersTimetables[teacher]=list.(emptyTimetable)
        choice=input("Done? (yes/no)")
    teachers12[i]=teachersList'''



#fixing fun periods