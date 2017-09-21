import datetime
print("_ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
print("\t\t BIRTHDAY APP")
print("_ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
print("Which year were you born [YYYY]?",end=' ')
year=int(input())
print("Which month were you born [MM]?",end=' ')
month=int(input())
print("Which day were you born [DD]?",end=' ')
day=int(input())
daysToBirthday=0
print(str("It seems like you were born on ") + str(day) +str("/") +str(month) + str("/") +str(year))
if daysToBirthday>0:
	print(str("\t Your birthday is in ") + str(daysToBirthday))
	print("We are looking forward to it!")
else:
	print("\t Your birthday is today.")
	print("Happy Birthday")

