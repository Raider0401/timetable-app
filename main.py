'''Harsh- Integrate SQL'''
'''Harsh- current date'''
'''Harsh- school name'''
'''Harsh- checkpoint'''
'''Harsh- excel sheet allow'''
'''Harsh- exception handling'''
'''Harsh- Implement Pandas and Matplotlib'''

#the following variables are useful throughout the project
emptyClassTemplate=[
    "", #Class teacher
    {}, #Teachers for subjects {"subject"="teacher name"}
    {}, #Number of periods per week per subject {"subject"=number}
    [[None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None]]
]

emptyTeacherTemplate=[
    "", #First name
    "", #Last name
    "", #Gender
    [False, ""], #Class teacher(yes/no), Class name
    0, #Workload 
    [[None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None]]
]

alphabet=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

#following section gathers info regarding classes and sections
print("please specify information regarding sections")
#exception handing if >26'''
#arrange for english vs English'''

timetables12={}
timetables11={}
timetables10={}
timetables9={}

teachersList={}
teachersTimetables={}
placeTimetables={}

#the followoing section of code gathers information regarding sections of grade 12
num12Sec=int(input("Please enter the number of sections in grade 12th: "))
for i in range(num12Sec):
    timetables12[alphabet[i]]=list(emptyClassTemplate)
print("Please enter the subjects for grade 12")
for section in timetables12.keys():
    print("Please enter the subejcts for section",section,":")
    subjects=[]
    checkpoint=False
    while checkpoint==False:
        choice=int(input("1) Preset of PCM[English, Physics, Chemistry, Maths, Optional]\
                     2) Preset of PCB[English, Physics, Chemistry, Maths, Optional]\
                     3) Preset of Commerce(with maths)[English, Physics, Chemistry, Maths, Optional]\
                     4) Preset of Commerce(without maths)[English, Physics, Chemistry, Maths, Optional]\
                     5) Preset of Humanities[English, Physics, Chemistry, Maths, Optional]\
                     6) Add a subject\
                     7) Remove a subject"))
        if choice==1:
            subjects=["english", "physics", "chemistry", "maths", "optional"]
        elif choice==2:
            subjects=["english", "physics", "chemistry", "maths", "optional"]
        elif choice==3:
            subjects=["english", "physics", "chemistry", "maths", "optional"]
        elif choice==4:
            subjects=["english", "physics", "chemistry", "maths", "optional"]
        elif choice==5:
            subjects=["english", "physics", "chemistry", "maths", "optional"]
        elif choice==6:
            subject=input("Please enter the subject to be included: ")
            subjects.append(subject.lower())
        elif choice==7:
            subject=input("Please enter the subject to be removed: ")
            if subject.lower() in subjects:
                subjects.remove(subject.lower())
            else:
                print("Subject is not in the list!")
        else:
            print("Please enter a valid response!")
        choice=input("Move to the next section? (yes/no): ")
        if choice.lower()=="yes":
            checkpoint=True
    
    for subject in subjects:
        subjectLoad=int(input("Please enter the number of periods per week for the subject {}: ".format(subject)))
        timetables12[section][1][subject]=""
        timetables12[section][2][subject]=subjectLoad
        if subject not in teachersList.keys():
            teachersList[subject]=[]

#the followoing section of code gathers information regarding sections of grade 11
num11Sec=int(input("Please enter the number of sections in grade 11th: "))
for i in range(num11Sec):
    timetables11[alphabet[i]]=list(emptyClassTemplate)
print("Please enter the subjects for grade 11")
for section in timetables11.keys():
    print("Please enter the subejcts for section",section,":")
    subjects=[]
    checkpoint=False
    while checkpoint==False:
        choice=int(input("1) Preset of PCM[English, Physics, Chemistry, Maths, Optional]\
                     2) Preset of PCB[English, Physics, Chemistry, Maths, Optional]\
                     3) Preset of Commerce(with maths)[English, Physics, Chemistry, Maths, Optional]\
                     4) Preset of Commerce(without maths)[English, Physics, Chemistry, Maths, Optional]\
                     5) Preset of Humanities[English, Physics, Chemistry, Maths, Optional]\
                     6) Add a subject\
                     7) Remove a subject"))
        if choice==1:
            subjects=["english", "physics", "chemistry", "maths", "optional"]
        elif choice==2:
            subjects=["english", "physics", "chemistry", "maths", "optional"]
        elif choice==3:
            subjects=["english", "physics", "chemistry", "maths", "optional"]
        elif choice==4:
            subjects=["english", "physics", "chemistry", "maths", "optional"]
        elif choice==5:
            subjects=["english", "physics", "chemistry", "maths", "optional"]
        elif choice==6:
            subject=input("Please enter the subject to be included: ")
            subjects.append(subject.lower())
        elif choice==7:
            subject=input("Please enter the subject to be removed: ")
            if subject.lower() in subjects:
                subjects.remove(subject.lower())
            else:
                print("Subject is not in the list!")
        else:
            print("Please enter a valid response!")
        choice=input("Move to the next section? (yes/no): ")
        if choice.lower()=="yes":
            checkpoint=True
    
    for subject in subjects:
        subjectLoad=int(input("Please enter the number of periods per week for the subject {}: ".format(subject)))
        timetables11[section][1][subject]=""
        timetables11[section][2][subject]=subjectLoad
        if subject not in teachersList.keys():
            teachersList[subject]=[]

#the follwoing section of code gathers information regarding sections of grade 10
num10Sec=int(input("Please enter the number of sections in grade 10th: "))
for i in range(num12Sec):
    timetables10[alphabet[i]]=list(emptyClassTemplate)
print("Please enter the subjects for grade 10")
for section in timetables10.keys():
    print("Please enter the subejcts for section",section,":")
    subjects=[]
    checkpoint=False
    while checkpoint==False:
        choice=int(input("1) Preset of PCM[English, Physics, Chemistry, Maths, Optional]\
                     2) Preset of PCB[English, Physics, Chemistry, Maths, Optional]\
                     3) Preset of Commerce(with maths)[English, Physics, Chemistry, Maths, Optional]\
                     4) Preset of Commerce(without maths)[English, Physics, Chemistry, Maths, Optional]\
                     5) Preset of Humanities[English, Physics, Chemistry, Maths, Optional]\
                     6) Add a subject\
                     7) Remove a subject"))
        if choice=="1":
            subjects=["english", "physics", "chemistry", "maths", "optional"]
        elif choice=="2":
            subjects=["english", "physics", "chemistry", "maths", "optional"]
        elif choice=="3":
            subjects=["english", "physics", "chemistry", "maths", "optional"]
        elif choice=="4":
            subjects=["english", "physics", "chemistry", "maths", "optional"]
        elif choice=="5":
            subjects=["english", "physics", "chemistry", "maths", "optional"]
        elif choice=="6":
            subject=input("Please enter the subject to be included: ")
            subjects.append(subject.lower())
        elif choice=="7":
            subject=input("Please enter the subject to be removed: ")
            if subject.lower() in subjects:
                subjects.remove(subject.lower())
            else:
                print("Subject is not in the list!")
        else:
            print("Please enter a valid response!")
        choice=input("Move to the next section? (yes/no): ")
        if choice.lower()=="yes":
            checkpoint=True
    
    for subject in subjects:
        timetables10[section][0][subject]=[]

        if subject not in teachersList.keys():
            teachersList[subject]=[]

#the follwoing section of code gathers information regarding sections of grade 9
num9Sec=int(input("Please enter the number of sections in grade 9th: "))
for i in range(num9Sec):
    timetables9[alphabet[i]]=list(emptyClassTemplate)
print("Please enter the subjects for grade 9")
for section in timetables9.keys():
    print("Please enter the subejcts for section",section,":")
    subjects=[]
    checkpoint=False
    while checkpoint==False:
        choice=int(input("1) Preset of PCM[English, Physics, Chemistry, Maths, Optional]\
                     2) Preset of PCB[English, Physics, Chemistry, Maths, Optional]\
                     3) Preset of Commerce(with maths)[English, Physics, Chemistry, Maths, Optional]\
                     4) Preset of Commerce(without maths)[English, Physics, Chemistry, Maths, Optional]\
                     5) Preset of Humanities[English, Physics, Chemistry, Maths, Optional]\
                     6) Add a subject\
                     7) Remove a subject"))
        if choice=="1":
            subjects=["english", "physics", "chemistry", "maths", "optional"]
        elif choice=="2":
            subjects=["english", "physics", "chemistry", "maths", "optional"]
        elif choice=="3":
            subjects=["english", "physics", "chemistry", "maths", "optional"]
        elif choice=="4":
            subjects=["english", "physics", "chemistry", "maths", "optional"]
        elif choice=="5":
            subjects=["english", "physics", "chemistry", "maths", "optional"]
        elif choice=="6":
            subject=input("Please enter the subject to be included: ")
            subjects.append(subject.lower())
        elif choice=="7":
            subject=input("Please enter the subject to be removed: ")
            if subject.lower() in subjects:
                subjects.remove(subject.lower())
            else:
                print("Subject is not in the list!")
        else:
            print("Please enter a valid response!")
        choice=input("Move to the next section? (yes/no): ")
        if choice.lower()=="yes":
            checkpoint=True
    
    for subject in subjects:
        timetables12[section][0][subject]=[]

        if subject not in teachersList.keys():
            teachersList[subject]=[]

#the following section of code gathers the list of teachers for every subject
print("Please try to fill in the following lists of teachers in the order of seniority")
for subject in teachersList.keys():
    teachersList[subject]=[]
    print("Please enter the information of teachers for subject:",subject)
    checkpoint=False
    while checkpoint==False:
        fName="Please enter the first name of the teacher: "
        lName="Please enter the last name of the teacher: "
        '''take care of input other that m/f'''
        gender="Please enter the gender of the teacher(M/F): "
        teachersList[subject].append(fName+" "+lName)
        teachersTimetables[fName+lName]=emptyTeacherTemplate
        teachersTimetables[fName+lName][0]=fName
        teachersTimetables[fName+lName][1]=lName
        teachersTimetables[fName+lName][2]=gender

#the following section of code attempts to assing teachers to various sections

print("Following gathers the information for grade 12")
for section in timetables12.keys():
    print("For grade 12",section, sep="")
    for subject in timetables12[section][1]:
        subjectLoad=timetables12[section][2][subject]
        print("Please choose a teacher for subject",subject,": ")
        serial=1
        for teacher in teachersList[subject]:
            print(serial, teacher, "Workload =",teachersTimetables[teacher][4])
            serial=serial+1
        checkpoint=False
        while checkpoint==False:
            teacherChoice=int(input("Please enter your choice: "))
            if teacherChoice not in range(1,serial):
                print("Please enter a value between 1 and",serial-1)
                continue
            teacherName=teachersList[subject][serial-2]
            workload=teachersTimetables[teacherName][4]
            if workload+subjectLoad>32:
                print(teacherName,"is overworked. Please chose another.")
            else:
                teachersTimetables[teacherName][4]+=subjectLoad
                timetables12[section][1][subject]=teacherName
                checkpoint=True
    candidates=[]
    for teacher in timetables12[section][1].values():
        if teachersTimetables[teacher][3][1]==False:
            candidate.append()
    print("Please select a class teacher from the following candidates: ")
    serial=1
    for candidate in candidates:
        print(serial,candidate)
        serial=serial+1
        checkpoint=False
        while checkpoint==False:
            teacherChoice=int(input("Please enter your choice: "))
            if teacherChoice not in range(1,serial):
                print("Please enter a value between 1 and",serial-1)
                continue
            else:
                teacher=candidates[serial-2]
                teachersList[teacher][3][0]=True
                teachersList[teacher][3][1]="12"+section
                timetables12[section][0]=teacher

print("Following gathers the information for grade 11")
for section in timetables11.keys():
    print("For grade 11",section, sep="")
    for subject in timetables11[section][1]:
        subjectLoad=timetables11[section][2][subject]
        print("Please choose a teacher for subject",subject,": ")
        serial=1
        for teacher in teachersList[subject]:
            print(serial, teacher, "Workload =",teachersTimetables[teacher][4])
            serial=serial+1
        checkpoint=False
        while checkpoint==False:
            teacherChoice=int(input("Please enter your choice: "))
            if teacherChoice not in range(1,serial):
                print("Please enter a value between 1 and",serial-1)
                continue
            teacherName=teachersList[subject][serial-2]
            workload=teachersTimetables[teacherName][4]
            if workload+subjectLoad>32:
                print(teacherName,"is overworked. Please chose another.")
            else:
                teachersTimetables[teacherName][4]+=subjectLoad
                timetables11[section][1][subject]=teacherName
                checkpoint=True
    candidates=[]
    for teacher in timetables11[section][1].values():
        if teachersTimetables[teacher][3][1]==False:
            candidate.append()
    print("Please select a class teacher from the following candidates: ")
    serial=1
    for candidate in candidates:
        print(serial,candidate)
        serial=serial+1
        checkpoint=False
        while checkpoint==False:
            teacherChoice=int(input("Please enter your choice: "))
            if teacherChoice not in range(1,serial):
                print("Please enter a value between 1 and",serial-1)
                continue
            else:
                teacher=candidates[serial-2]
                teachersList[teacher][3][0]=True
                teachersList[teacher][3][1]="11"+section
                timetables11[section][0]=teacher

print("Following gathers the information for grade 10")
for section in timetables10.keys():
    print("For grade 10",section, sep="")
    for subject in timetables12[section][1]:
        subjectLoad=timetables12[section][2][subject]
        print("Please choose a teacher for subject",subject,": ")
        serial=1
        for teacher in teachersList[subject]:
            print(serial, teacher, "Workload =",teachersTimetables[teacher][4])
            serial=serial+1
        checkpoint=False
        while checkpoint==False:
            teacherChoice=int(input("Please enter your choice: "))
            if teacherChoice not in range(1,serial):
                print("Please enter a value between 1 and",serial-1)
                continue
            teacherName=teachersList[subject][serial-2]
            workload=teachersTimetables[teacherName][4]
            if workload+subjectLoad>32:
                print(teacherName,"is overworked. Please chose another.")
            else:
                teachersTimetables[teacherName][4]+=subjectLoad
                timetables10[section][1][subject]=teacherName
                checkpoint=True
    candidates=[]
    for teacher in timetables10[section][1].values():
        if teachersTimetables[teacher][3][1]==False:
            candidate.append()
    print("Please select a class teacher from the following candidates: ")
    serial=1
    for candidate in candidates:
        print(serial,candidate)
        serial=serial+1
        checkpoint=False
        while checkpoint==False:
            teacherChoice=int(input("Please enter your choice: "))
            if teacherChoice not in range(1,serial):
                print("Please enter a value between 1 and",serial-1)
                continue
            else:
                teacher=candidates[serial-2]
                teachersList[teacher][3][0]=True
                teachersList[teacher][3][1]="10"+section
                timetables10[section][0]=teacher

print("Following gathers the information for grade 9")
for section in timetables9.keys():
    print("For grade 9",section, sep="")
    for subject in timetables9[section][1]:
        subjectLoad=timetables9[section][2][subject]
        print("Please choose a teacher for subject",subject,": ")
        serial=1
        for teacher in teachersList[subject]:
            print(serial, teacher, "Workload =",teachersTimetables[teacher][4])
            serial=serial+1
        checkpoint=False
        while checkpoint==False:
            teacherChoice=int(input("Please enter your choice: "))
            if teacherChoice not in range(1,serial):
                print("Please enter a value between 1 and",serial-1)
                continue
            teacherName=teachersList[subject][serial-2]
            workload=teachersTimetables[teacherName][4]
            if workload+subjectLoad>32:
                print(teacherName,"is overworked. Please chose another.")
            else:
                teachersTimetables[teacherName][4]+=subjectLoad
                timetables12[section][1][subject]=teacherName
                checkpoint=True
    candidates=[]
    for teacher in timetables9[section][1].values():
        if teachersTimetables[teacher][3][1]==False:
            candidate.append()
    print("Please select a class teacher from the following candidates: ")
    serial=1
    for candidate in candidates:
        print(serial,candidate)
        serial=serial+1
        checkpoint=False
        while checkpoint==False:
            teacherChoice=int(input("Please enter your choice: "))
            if teacherChoice not in range(1,serial):
                print("Please enter a value between 1 and",serial-1)
                continue
            else:
                teacher=candidates[serial-2]
                teachersList[teacher][3][0]=True
                teachersList[teacher][3][1]="9"+section
                timetables9[section][0]=teacher

#the following section of code actually generates the timetable
print("for grade 12")
for section in timetables12.keys():
    timetable=timetables12[section][3]
    for day in timetable:
        dayindex=timetable.index(day)
        subjects=timetable[1].keys()
        i=0
        for period in day:
            periodindex=day.index(period)
            subject=subjects[i]
            teacher=section[subject][5]
            while period==None:
                if teacher[dayindex][periodindex]==None:
                    teacher[dayindex][periodindex]="12"+section
                    timetable[dayindex][periodindex]=subject
                    i+=1
                else:
                    i+=1
    print("12"+section)
    print(timetable)

print("for grade 11")
for section in timetables11.keys():
    timetable=timetables11[section][3]
    for day in timetable:
        dayindex=timetable.index(day)
        subjects=timetable[1].keys()
        i=0
        for period in day:
            periodindex=day.index(period)
            subject=subjects[i]
            teacher=section[subject][5]
            while period==None:
                if teacher[dayindex][periodindex]==None:
                    teacher[dayindex][periodindex]="11"+section
                    timetable[dayindex][periodindex]=subject
                    i+=1
                else:
                    i+=1
    print("11"+section)
    print(timetable)

print("for grade 10")
for section in timetables10.keys():
    timetable=timetables10[section][3]
    for day in timetable:
        dayindex=timetable.index(day)
        subjects=timetable[1].keys()
        i=0
        for period in day:
            periodindex=day.index(period)
            subject=subjects[i]
            teacher=section[subject][5]
            while period==None:
                if teacher[dayindex][periodindex]==None:
                    teacher[dayindex][periodindex]="10"+section
                    timetable[dayindex][periodindex]=subject
                    i+=1
                else:
                    i+=1
    print("10"+section)
    print(timetable)

print("for grade 9")
for section in timetables9.keys():
    timetable=timetables9[section][3]
    for day in timetable:
        dayindex=timetable.index(day)
        subjects=timetable[1].keys()
        i=0
        for period in day:
            periodindex=day.index(period)
            subject=subjects[i]
            teacher=section[subject][5]
            while period==None:
                if teacher[dayindex][periodindex]==None:
                    teacher[dayindex][periodindex]="9"+section
                    timetable[dayindex][periodindex]=subject
                    i+=1
                else:
                    i+=1
    print("9"+section)
    print(timetable)
