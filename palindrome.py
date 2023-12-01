def isPalindrome(n):
 n_str=str(n)
 n_rev=n_str[::-1]
 if(n_str==n_rev):
   return True
 return False
n=str(input("enter a string:"))
result=isPalindrome(n)
if(result==True):
	print(n,"is a palindrome string")
else:
	print(n,"is not a palindrome string")
