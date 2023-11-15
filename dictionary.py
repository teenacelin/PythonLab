n = int(input("Enter number of students: "))
result = {}
for i in range(n):
	print("Enter Details of student No.", i+1)
	rno = int(input("Roll No: "))
	name = input("Name: ")
	age = input("Age: ")
	grade = (input("Grade: "))
	address=input("Address: ")
	result[rno] = [name,age, grade,address]
	print(result)

