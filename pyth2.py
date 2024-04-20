"""
fruits=['apple','mango','grape','orange']
for i in fruits:
    if(i=='mango'):
        continue
    print(i)
for i in range(10,40,5):
    print(i)

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=' ')
    print(' ')
def hi():
    print("Hello")
hi()
def evenodd(num):
    if(num%2==0):
        print("Even number")
    else:
        print("odd number")
num=int(input("Enter the number:"))
#evenodd(num)
if num==1:
    print("prime")
elif num>1:
    for i in range(2,num):
        if(num%i==0):
            print("not prime")
            break
    else:
        print("prime")
else:
    print("Not prime")
"""
x=lambda a:a+10
print(x(8))

class Num:
    x=5
p1=Num()
print(p1.x)

class person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def print(self):
        print(self.firstname,self.lastname)
x=person("Aleena","Sijoy")
x.print()

class student(person):
    pass
x=student("Aneeta","Sijoy")
x.print()