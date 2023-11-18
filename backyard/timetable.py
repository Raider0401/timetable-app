#sectionNum=4

#A=[["English","Physics","Chemistry","Maths","Optional"],["PD","Assembly","Library", "Club"]]
#B=[["English","Physics","Chemistry","Maths","Optional"],["PD","Assembly","Library", "Club"]]
#C=[["English","Physics","Chemistry","Biology","Optional"],["PD","Assembly","Library", "Club"]]
#D=[["English","Accounts","BST","Eco","Optional"],["PD","Assembly","Library", "Club"]]
#E=[["English","History","Geography","Pol Science","Optional"],["PD","Assembly","Library", "Club"]]

A=[
    ["CTP", None, None, None, None, "PD", "Break", "Optional", "Optional", None, None],
    ["CTP", "Assembly", None, None, None, None, "Break", "Optional", None, None, None],
    ["CTP", None, None, None, None, None, "Break", "Optional", "Optional", "Library", None],
    ["CTP", None, None, None, None, None, "Break", "Optional", None, None, None],
    ["CTP", None, None, "Optional", "Optional", "PD", "Break", None, None, None, None],
    ]

#User gets to choose
#a[2][1]=b[2][1]=c[2][1]=d[2][1]=e[2][1]="Assembly"
physics={"A":"Mr. Rahul","B":"Mr. Mohan"}
chemistry={"A":"Ms. Parul"}
maths={"A":"Mr. Manoj"}
english={"A":"Ms. Sadaf"}
subjects=[physics, chemistry, maths, english]

section=A
for day in section:
    for i in day:
        for subject in subjects:
            if i!=None and subjects[subject][str(section)][day.index()][i.index()]==None:
                subjects[subject][str(section)][day.index()][i.index()]=str(section)