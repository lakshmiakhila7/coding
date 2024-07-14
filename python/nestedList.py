# here are  students in this class whose names and grades are assembled to build the following list:
# python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# The lowest grade of  belongs to Tina. The second lowest grade of  belongs to both Harry and Berry, 
# so we order their names alphabetically and print each name on a new line.
if __name__ == '__main__':
    records=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
x= [x[1] for x in records]
mini = sorted(set(x))
y = sorted([y[0] for y in records if y[1]==mini[1]])
[print(k) for k in y]
