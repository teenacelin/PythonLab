print("enter the binary number:")
bnum=int(input())
dnum=0
i=1
while bnum!=0:
	rem=bnum%10
	dnum=dnum+(rem*i)
	i=i*2
	bnum=int(bnum/10)
print("\n equilvalent decimal value is=",dnum)
