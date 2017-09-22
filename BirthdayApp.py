from datetime import date
print("_ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")
print("\t\tBIRTHDAY APP")
print("_ _ _ _ _ _ __ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")

def InputBirthday():
	print("What year were you born [YYYY]?",end=' ')
	year=int(input())
	print("What month were you born [MM]?",end=' ')
	month=int(input())
	print("What day were you born [DD]?",end=' ')
	day=int(input())
	MyBirthday=date(year,month,day).strftime("%m/%d/%Y")
	print(str("It looks like you were born on ") + str(MyBirthday) )
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
		print(str("Looks like your birthday is in ") + str(DaysToBirthday.days) + str(" days."))
		print("Hope you're looking forward to it!")
	else:
		DaysToBirthday=abs(MyBirthday-Today)
		print(str("Looks like your birthday is in ") + str(DaysToBirthday.days) + str(" days."))
		print("Hope you're looking forward to it!")


DaysToBirthday()
	
		
