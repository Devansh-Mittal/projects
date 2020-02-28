n=int(input("Enter the no. of entries"))
marksheet=[]
for i in range(0,n):
    marksheet.append([input(),float(input())])

print(marksheet)
def sortsecond(element):
    return element[1]
marksheet.sort(key=sortsecond)
print(marksheet)
h=marksheet.pop()
print(marksheet)
for i in marksheet():
    g=marksheet.pop
