from datetime import date
print("_ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
<<<<<<< HEAD
print("\t\tBIRTHDAY APP")
=======
print("\t\t BIRTHDAY APP")
>>>>>>> bed5297ea85f9834e2e5b5a29ad909b323e08495
print("_ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")

def InputBirthday():
	print("Which year were you born [YYYY]?",end=' ')
	year=int(input())
	print("Which month were you born [MM]?",end=' ')
	month=int(input())
	print("Which day were you born [DD]?",end=' ')
	day=int(input())
	MyBirthday=date(year,month,day).strftime("%m/%d/%Y")
	print(str("It seems like you were born on ") + str(MyBirthday) )
	return day,month

def DaysToBirthday():
	Today=date.today()
	day,month=InputBirthday()
	MyBirthday=date(Today.year,month,day)
	if MyBirthday==Today:
		print("\t Your birthday is today.")
		print("Happy Birthday!")
	elif MyBirthday<Today:
		MyBirthday=MyBirthday.replace(year=Today.year+1)
		DaysToBirthday=abs(MyBirthday-Today)
		print(str("\t Your birthday is in ") + str(DaysToBirthday.days) + str(" days"))
		print("We are looking forward to it!")
	else:
		DaysToBirthday=abs(MyBirthday-Today)
		print(str("\t Your birthday is in ") + str(DaysToBirthday.days) + str(" days"))
		print("We are looking forward to it!")


DaysToBirthday()
	
		
