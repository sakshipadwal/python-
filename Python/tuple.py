from collections import namedtuple
a=namedtuple('courses','name,technology')
s=a('data science','python')
print(s)
from typing import Tuple

myTuple=(10,20,30)    #Tuple= Mix type of data
yourTuple=("Pune","Mumbai","Delhi")
mixTuple=('Foo',[1,2,3],'True')
nestedTuple=(("Wes McKinney","Python for Data Analysis","O'Reilly Media"),("Mark Lutz","Programming python","O'Reilly Media")
             ,("Charlies Severance","Python For Everybody","Blumenberg"))

#merge my tuple and your tuple into our tuple
ourTuple=myTuple+yourTuple
print("1) ourTuple=",ourTuple)

#Convert myTuple into list myList and reverse
myList=list(myTuple)
myList.sort()
print("2) Assending myList=",myList)
myList.reverse()
print("3) Reverse myList=",myList)

#Unpack yourTuple values into three variables-District,State and National
x,y,z=yourTuple
print("3) Unpacking of yourTuple into three variables:",yourTuple)
print("District=",x)
print("State=",y)
print("National=",z)

#Display all elements of mixTuple
print("4) mixTuple=",mixTuple)

#add 4 into list element of mixTuple
mixTuple[1].append(4)
print("5) Adding 4=",mixTuple)

#perform algebraic operations addition and multiplication

from operator import mul
add=myTuple+yourTuple
print("6) Addition=",add)
multi=tuple(map(mul,myTuple,yourTuple))
print("Multiplication=",multi)

#Access information from nestedTuple and
print("7) Unpacking:")
for a,b,c in nestedTuple:
    print(" Name of author=",a)
    print(" Name of Book=",b)
    print(" Name of Publisher=",c)
    print("")