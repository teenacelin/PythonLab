dic={}
n1=int(input("Total number of elements in dictionary : "))
for i in range(n1):
    dic[i]=input("Enter element : ")
print("Ascending order of elements:")
print(sorted(dic.items(), key = lambda kv:(kv[1], kv[0])))
print("Descending order of elements:")
print(sorted(dic.items(), key = lambda kv:(kv[1], kv[0]), reverse=True))





