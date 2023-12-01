num=int(input("enter the number to be checked:"))
sum=0
for i in range(1,num):
 if num%i==0:
  sum=sum+i
if sum==num:
  print("The number",num,"is perfect number")
else:
  print("the number",num,"is not a perfect number")
