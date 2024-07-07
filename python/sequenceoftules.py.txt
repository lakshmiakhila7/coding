 def Test(s,e):
    tuple_list=[(i,i**2) for i in range(s,e+1)]
    return tuple(tuple_list)
s=int(input())
e=int(input())
result=Test(s,e)
print(result)
