var=input("Enter the numnber (0-9 ):")
Target=int(input("Enter the number "))
var2=int(var[0])
var3=int(var[0])
for ele in range(1,len(var)):
    var2=var2+int(var[ele])
    var3=var3*int(var[ele])  
if var2==Target and var3==Target:
    ans1='"'+"+".join(var[i:i+1]for i in range(0,len(var),1))+'"'
    ans2='"'+"*".join(var[i:i+1]for i in range(0,len(var),1))+'"'
    last=set((ans2,ans1))
    print(last)
else:
    print("{ }")