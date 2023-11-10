num1=float(input("Enter the first number:"))
num2=float(input("enter the second number:"))
operation=input("choose an arithmetic operation(+,-,*,/,**,//,%):")
if operation=="+":
	result=num1+num2
elif operation=="-":
	result=num1-num2
elif operation=="*":
	result=num1*num2
elif operation=="/":
	result=num1/num2
elif operation=="**":
	result=num1**num2
elif operation=="//":
	result=num1//num2
elif operation=="%":
	result=num1%num2
else:
   print("invalid input")
print("the result is:",result)






