x=input("Enter first names:")
list=x.split(" ")
count=0
for i in list:
	for j in i:
		if 'a'==j or 'A'==j:
			count=count+1
print("the occurence of 'a' in the list is:",count)
