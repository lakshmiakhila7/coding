# The first line contains the integer , the number of students' records. 
#The next  lines contain the names and marks obtained by a student, each value separated by a space. 
#The final line contains query_name, the name of a student to query.
# Sample Input 0
# siz=3
#Krishna 67 68 69
#Arjun 70 98 63
#Malika 52 56 60
#Malika
#Sample Output 0
#56.00
#Explanation 0
#Marks for Malika are  whose average is 52+56+60/3=>56
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    x=sum(student_marks[query_name])/3
    y=format(x,".2f")
    print(y)
    
