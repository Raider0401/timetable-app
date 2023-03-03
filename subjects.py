from random import randint

#Taking a random set of subjects
subjects=["English","Maths","CS","Social Science","Science","Spanish","PD"]
num_accurate=[]
for i in subjects:
    if i in ["Maths","CS","Social Science","Science"]:
        for j in range(6):
            num_accurate.append(i)
    elif i=="PD":
        for j in range(2):
            num_accurate.append(i)
    else:
        for j in range(7):
            num_accurate.append(i)
print(num_accurate)

weekdays=["Monday","Tuesday","Wednesday","Thursday","Friday",]
for day in weekdays:
    day=[]
    list=[-1]
    while len(list)<8:
        x=randint(0,len(subjects)-1)
        #Mechanism of combining two subjects if they occur twice on the same day
        if x in list:
            if list.count(x)==2:
                continue
            else:
                list.insert(list.index(x)+1,x)
        else:
            list.append(x)

    list.insert(4,-2)    

    for i in list:
        if i==-1:
            day.append("CTP")
        elif i==-2:
            day.append("Break")
        else:
            day.append(subjects[i])

    print(day)