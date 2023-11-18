rahul=[
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None]
]
parul=[
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None]
]
manoj=[
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None]
]
sadaf=[
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None]
]
optional=[
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None]
]

A=[
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None],
    [None,None,None,None,None,"Break",None,None,None,None]
]

a={"physics":rahul, "chemistry":parul, "maths":manoj, "english":sadaf, "optional":optional}

subjects=["physics","chemistry","maths","english","optional"]
section=a

for day in A:
    dayindex=A.index(day)
    i=0
    for period in day:
        if i>4:
            break
        periodindex=day.index(period)
        subject=subjects[i]
        teacher=section[subject]
        while period==None:
            if teacher[dayindex][periodindex]==None:
                period=A[dayindex][periodindex]=subject
                i+=1
            else:
                i+=1

print(A)
