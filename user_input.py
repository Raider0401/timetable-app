#Input Grade and Section
grade= input("Enter grade: ")
section=input("Enter section: ")
print()

#Input no. of subjects
num_main_sub= int(input("Enter number of mainstream subjects: "))
num_extra_sub= int(input("Enter number of co-curricular activities: "))
print()

#Input no. of periods in a day
num_period=int(input("Enter number of periods in a day: "))

#If there are any fixed periods everyday
fixed_period_bool=input("Does the school have any periods that ocurr at the same time throughout the week (for eg: Class Teacher Period at the beginning of the day): ")
print()

dict_fixed_period={} # Dictionary contains fixed periods and their duration (in min).
if "Y" in fixed_period_bool or "y" in fixed_period_bool: #If the timetable has fixed periods then how many and are all fixed periods of the same time interval.
    num_fixed_period=int(input("Enter no. of fixed periods per day: "))
    time_fixed_period_bool=input("Does each fixed period have the same timing? (Y or N): ")
    print()
    
    # Same timings.
    if "Y" in time_fixed_period_bool or "y" in time_fixed_period_bool:
        time_fixed_period=int(input("Enter duration (in min) of each period: "))
        for i in range(1,num_fixed_period+1):
            fixed_period=input(f"Enter the name of fixed period {i}: " )
            dict_fixed_period[fixed_period]=time_fixed_period

        # Timings differ.
    else:
        for i in range(1,num_fixed_period+1):
            fixed_period=input(f"Enter the name of fixed period {i}: " )
            time_fixed_period=int(input(f"Enter duration (in min) of period {i}: "))
            dict_fixed_period[fixed_period]=time_fixed_period
            print()
print()
print("The fixed period dictionary is:",dict_fixed_period) #prints the fixed periods dictionary.
print()

# Main subject dictionary with time

sub_main_dict={} # Contains the name of the subjects and their duration (in min).
equal_time_bool= input("Is the duration for all the main subjects same?(answer in Y or N) ")

if "Y" in equal_time_bool  or "y" in equal_time_bool:
    time_slot=int(input("Enter duration (in min) between each period: "))
    print()
    for i in range(1,num_main_sub+1): # Inputs duration of each subject alongwith the subject name.
        subject=input(f"Enter the name of subject {i}: ")
        sub_main_dict[subject]=time_slot
        
else: # Different duration.
    for i in range(1,num_period+1): # Inputs duration of each subject alongwith the subject name.
        subject=input(f"Enter the name of main subject {i}: ")
        time_slot=int(input(f"Enter duration (in min) of {subject}: "))
        sub_main_dict[subject]=time_slot
        print()
print()      
print("The dictionary with all the main subjects and their time",sub_main_dict)
print()

# Co-curricular activity dictionary with time

co_dict={} # Contains the name of the activity and their duration (in min).
equal_time_bool= input("Is the duration for all the co-curricular activity period same?(answer in Y or N) ")
if equal_time_bool == "Y" or equal_time_bool== "y":
    time_bool= input("Is the duration for co-curricular activity periods same as that of main subjects: ")
print()

if time_bool == "Y" or time_bool== "y":
    for i in range(1,num_extra_sub+1): # Inputs duration of each activity alongwith the subject name.
        activity_name=input(f"Enter the name of the activity {i}: ")
        co_dict[activity_name]=time_slot

else: # Different duration.
    for i in range(1,num_period+1): # Inputs duration of each activity alongwith the activity name.
        activity_name=input(f"Enter the name of the activity {i}: ")
        time_slot=int(input(f"Enter duration (in min) of {activity_name}: "))
        co_dict[activity_name]=time_slot
        print()

print()
print("The dictionary with all the activities and their time",co_dict)


