pas=input("enter the password")
l,k,m,p=0,0,0,0
for i in pas:
    if (i.isupper()):
        l+=1
    if (i.islower()):
        k+=1
    if (i.isdigit()):
        m+=1
    if(i=='@' or i=='$' or i=='_'):
        p+=1
if(l>=1 and k>=1 and m>=1 and p>=1 and l+k+m+p==len(pas)):
    print("valid pass")
else:
    print("invalid passworad")
