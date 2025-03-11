assign_grade=int(input("What is your grade or score?: "))

if assign_grade>100 or assign_grade<0:
	print("Invalid score! Please enter a value between 0 and 100")
elif assign_grade>=90:
	print("Grade: A")
elif assign_grade>=80:
	print("Grade: B ")
elif assign_grade>=70:
	print("Grade: C")
elif assign_grade>=60:
	print("Grade: F")
else:
	print("Invalid score! Please enter a value between 0 and 100")