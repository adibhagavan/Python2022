>>> x=0
>>> y=20
>>> x+y
20
>>> print("x=y",str(x+y))
x=y 20
>>> print("x=y",x+y)
x=y 20
>>> x=100
>>> y=10
>>> z=x*y
>>> z
1000
>>> z1=x/y
>>> z1
10.0
>>> a=2000
>>> a=a/y
>>> a
200.0
>>> x:int=100
>>> y=str(x)
>>> print("datatype of x", type(x))
datatype of x <class 'int'>
>>> print("datatype of y", type(y))
datatype of y <>>> print("4. Prove Python has dynamic inference feature")

4. Prove Python has dynamic inference feature
>>> x=10
>>> x=y
>>> type(x)
<class 'str'>
>>> x=10
>>> type(x)
<class 'int'>class 'str'>

>> > print("5. Prove Python is Strongly Typed Language")

5. Prove Python is Strongly Typed Language
>>> x=10
>>> y='y is string"
  File "<stdin>", line 1
    y='y is string"
                  ^
SyntaxError: EOL while scanning string literal
>>> y="y is string"
>>> z=x+y
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> z=str(x)+str(y)
>>> z
'10y is string'
>>> print("6. Create variables a,b,c,d assigned with 10,20,30,40 respectively")

6. Create variables a,b,c,d assigned with 10,20,30,40 respectively
>> > a, b, c, d = 10, 20, 30, 40
>> > a
10
>> > b
20
>> > c
30
>> > d
40
>>> print("7. Prove Python variables are case sensitive")

7. Prove Python variables are case sensitive
>>> A
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'A' is not defined
>>> a
10
>>> Print("P is caps in Print")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Print' is not defined
>>> print("P is caps in Print")
P is caps in Print
>>> print("8. Prove variable name can't start with numbers or cannot contains sp
ecial character other than _ ")

8. Prove variable name can't start with numbers or cannot contains special chara
cter other than _
>>> 1_var =10
  File "<stdin>", line 1
    1_var =10
     ^
SyntaxError: invalid token
>>> var_1=10
>>> var@1=10
  File "<stdin>", line 1
SyntaxError: can't assign to operator
>>> var!1=10
  File "<stdin>", line 1
    var!1=10
       ^
SyntaxError: invalid syntax

>>> print("9. Show some examples of when do we use single, double and triple (si
ngle/double) quotes")
9. Show some examples of when do we use single, double and triple (single/double
) quotes
>>> x="Adi"
>>> print(x)
Adi
>>> x='adi'
>>> print(x)
adi
>>> x='"adi","bhagavan"'
>>> print(x)
"adi","bhagavan"
>>> x="'adi','bhagavan'"
>>> print(x)
'adi','bhagavan'

>>> print("10. Show an examples to use arithmetic, comparison, relational and lo
gical operators.")
10. Show an examples to use arithmetic, comparison, relational and logical opera
tors.

>>> if x==10:
...     print("x=10")
... else:
...     print("x<>10")
...
x=10

>>> x,y=10,10
>>> if x==y:
...     print("x is equal to y")
... else:
...     print("x is not equal to y"
...
...     )
...
x is equal to y
>>> x,y=10,20
>>> if x==y:
...     print("x is equal to y")
... else:
...     print("x is not equal to y")
...
x is not equal to y
>>>

10. Show an examples to use arithmetic, comparison, relational and logical operators.

>>> def calc_sum_sal(sal_list,dept,revenue): #Function based programming
...     sal=0 #assignement operator
...     dept1='IT'
...     for i in sal_list: #control structures - looping construct
...             sal=sal+i #assignment and arithmetic operators
...     if (sal > revenue and dept1==dept): #control structures - conditional st
ructure, relation operator, logical operator
...
...             print("we have a loss of "+ str(sal-revenue)) #Strongly typed va
riable, converting to str() to operate with another string
...     else:
...             print("we got a profit of "+ str(revenue-sal))
...
>>> calc_sum_sal(sal_list,'IT',1000000)
we got a profit of 895000
>>> calc_sum_sal(sal_list,'IT',100000)
we have a loss of 5000

>>> print("11. Write a program to find the greatest of 3 numbers")
11. Write a program to find the greatest of 3 numbers
>>> x,y,z=10,20,30
>>> if(x==y==z):
...     print("x=y=z")
... elif(x>y and x>z):
...     print("x is greater than y and z")
... elif(y>x and y>z):
...     print("y is greater than x and z")
... else:
...     print("z is greater than x and y")
...
z is greater than x and y

>>> def greatest(x,y,z):
...     if(x==y==z):
...             print("x=y=z")
...     elif(x>y and x>z):
...             print("x is greater than y and z")
...     elif(y>x and y>z):
...             print("y is greater than x and z")
...     else:
...             print("z is greater than x and y")
...
>>> greatest(30,20,12)
x is greater than y and z
>>> greatest(10,50,20))
  File "<stdin>", line 1
    greatest(10,50,20))
                      ^
SyntaxError: invalid syntax
>>> greatest(10,50,20)
y is greater than x and z
>>> greatest(10,50,60)
z is greater than x and y

print("12. Write a single program to find the given number is even or whether it is negative and print the output as (the given number is even but not "
      "negative or the given number is not even but negative or the given number is neither negative nor even) ")
def find_even_negative(x):
  if x%2==0 and x >= 0:
    print(f"{x} is even and non-negative")
  elif x%2==0 and x < 0:
    print(f"{x} is even and negative")
  elif x%2!=0 and x<0:
    print(f"{x} is not even but negative")
  elif x%2!=0 and x >= 0:
    print(f"{x} is neither negative nor even")

>>> find_even_negative(-20)
-20 is even and negative
>>> find_even_negative(10)
10 is even and non-negative
>>> find_even_negative(-10)
-10 is even and negative
>>> find_even_negative(11)
11 is neither negative nor even
>>> find_even_negative(-11)
-11 is not even but negative

print("13.Write a nested if then else to print the course fees - check if student choosing bigdata, then fees is 25000, "
      "if student choosing spark then fees is 15000, if the student choosing datascience then check if machinelearning then 25000 "
      "or if deep learning then 45000 otherwise if both then 25000+25000.")
13.Write a nested if then else to print the course fees - check if student choos
ing bigdata, then fees is 25000, if student choosing spark then fees is 15000, i
f the student choosing datascience then check if machinelearning then 25000 or i
f deep learning then 45000 otherwise if both then 25000+25000.
def find_coursefee(cname,subcourse):
  if cname =="bigdata":
    return 25000
  elif cname == "spark":
    return 15000
  elif cname == "datascience":
    if subcourse== "machinelearning":
      return 25000
    elif subcourse == "deep_learning":
      return 45000
    elif subcourse =="both":
      return 25000+25000

>>> find_coursefee("bigdata","")
25000
>>> find_coursefee("spark","")
15000
>>> find_coursefee("datascience","")
>>> find_coursefee("datascience","machinelearning")
25000
>>> find_coursefee("datascience","deep_learning")
45000
>>> find_coursefee("datascience","both")
50000

print('14. Check whether the given string is palindrome or not (try to use some function like reverse). '
      'For eg: x="madam" and y="madam", if x matches with y then print as "palindrome" else "not a  palindrome".')
14. Check whether the given string is palindrome or not (try to use some functio
n like reverse). For eg: x="madam" and y="madam", if x matches with y then print
 as "palindrome" else "not a  palindrome".

>>> def checkpalindrome(x_str):
...     if x_str==x_str[::-1]:
...             print(f"{x_str} is a palindrome")
...     else:
...             print(f"{x_str} is not a palindrome")
...
>>> checkpalindrome("malayalam")
malayalam is a palindrome
>>> checkpalindrome("malayala")
malayala is not a palindrome
>>> checkpalindrome("radar")
radar is a palindrome
>>> checkpalindrome("naman")
naman is a palindrome

>>> print("15. Check whether the x=100 is an integer or string. (try to use some
 functions like str or upper function etc to execute this use case) or use isins
tanceof(variablename,datatype) function.")
15. Check whether the x=100 is an integer or string. (try to use some functions
like str or upper function etc to execute this use case) or use isinstanceof(var
iablename,datatype) function.

>>> x=100
>>> type(x)
<class 'int'>
>>> isinstance(x,int)
True
>>> isinstance(x,str)
False
>>> isinstance(x,float)
False

##Collections: List, Dictionary, Tuple and Set
>>> print("16. Create a list with a range of 10 values starting from 2 to 11 and
 prove mutability by updating the 3rd element with 100 and prove resizable prope
rties by adding 100 in the 5th position.")
16. Create a list with a range of 10 values starting from 2 to 11 and prove muta
bility by updating the 3rd element with 100 and prove resizable properties by ad
ding 100 in the 5th position.
>>>
>>> listval=[2,3,4,5,6,7,8,9,10,11]
>>> listval[2] = 100
>>> listval
[2, 3, 100, 5, 6, 7, 8, 9, 10, 11]
>>> listval.insert(5,100)
>>> listval
[2, 3, 100, 5, 6, 100, 7, 8, 9, 10, 11]

>>> print('17. Create a tuple of 2 fields eg. ("Inceptez","Technologies","Pvt","
Ltd"), prove immutability and non resizable nature, access the 2nd and 4th field
s and store in another tuple.')
17. Create a tuple of 2 fields eg. ("Inceptez","Technologies","Pvt","Ltd"), prov
e immutability and non resizable nature, access the 2nd and 4th fields and store
 in another tuple.
>>>
>>> tup1=("Inceptez","Technologies","Pvt","Ltd")
>>> tup1
('Inceptez', 'Technologies', 'Pvt', 'Ltd')
>>> tup2=(tup1[1],tup1[3])
>>> tup2
('Technologies', 'Ltd')
>>> tup2[1]="updated"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> tup2.insert(4,"updated")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'insert'
>>>

18. Convert the list of tuples [("Inceptez","Technologies"),("Apple","Incorporation")] to list of dictionary type, using for loop as given below
[{"Inceptez":"Technologies"},{"Apple":"Incorporation"}] , once the list of dictionary is arrived print only "Incorporation" by passing "Apple" as a key
using dict["Apple"] and dict.get("Apple") and try with dict["Apple1"] and dict.get("Apple1") then find the difference between get and using[] notation.

>>> dict1=dict()
>>> for i in tup3:
...      dict1[i[0]]=i[1]
...      print(dict1)
...
{'Inceptez': 'Technologies'}
{'Inceptez': 'Technologies', 'Apple': 'Incorporation'}
>>> dict1["Apple"]
'Incorporation'
>>> dict1.get("Apple")
'Incorporation'
>>> dict1["Apple1"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'Apple1'
>>> dict1.get("Apple1")

>>> print('19. Create a list of tuple as given below and delete all duplicate tu
ples of the list  lst=[("Inceptez","Technologies"),("Apple","Incorporation"),("I
nceptez","Technologies"),("Inceptez","Technologies")]')
19. Create a list of tuple as given below and delete all duplicate tuples of the
 list  lst=[("Inceptez","Technologies"),("Apple","Incorporation"),("Inceptez","T
echnologies"),("Inceptez","Technologies")]
>>> lst=[("Inceptez","Technologies"),("Apple","Incorporation"),("Inceptez","Tech
nologies"),("Inceptez","Technologies"),("Adi","WD23")]
>>> dis_lst=[t for t in (set(tuple(i) for i in lst))]
>>> dis_lst1=list(set(tuple(i) for i in lst))
>>> print(str(dis_lst))
[('Adi', 'WD23'), ('Apple', 'Incorporation'), ('Inceptez', 'Technologies')]
>>> print(str(dis_lst1))
[('Adi', 'WD23'), ('Apple', 'Incorporation'), ('Inceptez', 'Technologies')]
>>> dis_lst.append(("Intel","Corp"))
>>> print(str(dis_lst))
[('Adi', 'WD23'), ('Apple', 'Incorporation'), ('Inceptez', 'Technologies'), ('In
tel', 'Corp')]


>>> print('21. Convert the lst_dict= [{"Inceptez":"Technologies"},{"Apple":"Inco
rporation"}] to lst1=["Inceptez","Apple"] , think about using for loop, list() f
unction, keys function and list append functions to achieve this.')
21. Convert the lst_dict= [{"Inceptez":"Technologies"},{"Apple":"Incorporation"}
] to lst1=["Inceptez","Apple"] , think about using for loop, list() function, ke
ys function and list append functions to achieve this.

>>> lst_dict= [{"Inceptez":"Technologies"},{"Apple":"Incorporation"}]
>>> lst_dict= [{"Inceptez":"Technologies"},{"Apple":"Incorporation"}]
>>> lst =list()
>>> for i in lst_dict:
...     lst= lst + list(i.keys())
...     print(str(lst))
...
['Inceptez']
['Inceptez', 'Apple']
>>> lst =list()
>>> for i in lst_dict:
...     lst.append(list(i.keys()))
...     print(str(lst))
...
[['Inceptez']]
[['Inceptez'], ['Apple']]
>>>

print('22. Create a list of values lst=[10,20,40,30,20], find the first, last values of the list, sort the list in '
      'ascending order, sort in descending order, print the minumum and maximum values of the descending sorted list, '
      'find the sum of all elements in the list, remove the number 30 and 20 from the list.')
lst=[10,20,40,30,20]
lst.sort()
print(f"First element in list is {str(lst[0])} and last element value is {lst[lst.__len__()-1]}")
print(str(lst))
lst.reverse()
print(str(lst))
print(f"max amount in list is {str(lst[0])}, min amount in list is {lst[lst.__len__()-1]} ")
Total=int()
for i in lst:
    Total=Total+i
print(Total)
print(str(lst))
lst.remove(30)
lst.remove(20)
print(str(lst))
>>> print (f"min of tup is {tmp_lst[0]} and max of tup is {tmp_lst[tmp_lst.__len
__()-1]}")
min of tup is 10 and max of tup is 40
23. Do the above same (step 25) operation in the tuple of elements tup=(10,20,40
,30,20)
>>> tup=(10,20,40,30,20)
>>> tup[0]
10
>>> tup.sort()
>>> tup
(10, 20, 40, 30, 20)
>>> tmp_lst=list(tup)
>>> tmp_lst
[10, 20, 40, 30, 20]
>>> tmp_lst[0]
10
>>> tmp_lst[tmp_lst.__len__()-1]
20
>>> tmp_lst.sort()
>>> tmp_lst[tmp_lst.__len__()-1]
40
>>> tmp_lst.reverse()
>>> tmp_lst
[40, 30, 20, 20, 10]
>>> tmp_lst.sort()

24. Convert the string to list from str1="Inceptez Technologies Pvt Ltd" to lst_str1=['Inceptez', 'Technologies', 'Pvt', 'Ltd']
str1="Inceptez Technologies Pvt Ltd"
str2 = str1.split(' ')
print(str2)
print("'24. Convert the string to list from str1="Inceptez Technologies Pvt Ltd" to lst_str1=['Inceptez', 'Technologies', 'Pvt', 'Ltd']'")

25. With the below given data in the format of list(list(elements))
emplstlst= [["1", ("Arun","Kumar"), "10000"],["2", ("Bala","Mohan"), "12000"]]

Display the below output for all of the 5 given simple scenarios
a. Convert the first element of the above list into tuple
("1", ("Arun","Kumar"), "10000")
b. Print the second element's second element and reverse the first and last name as given below
("Mohan","Bala")
c. Convert the emplstlst into tuples(tuples)
emplstlst= (("1", ("Arun","Kumar"), "10000"),("2", ("Bala","Mohan"), "12000"))
d. Add all salary of the above list
22000

>>> emplstlst= [["1", ("Arun","Kumar"), "10000"],["2", ("Bala","Mohan"), "12000"
]]
>>> emplstlst[0]
['1', ('Arun', 'Kumar'), '10000']
>>> tup1=list( emplstlst[0])
>>> tup1
['1', ('Arun', 'Kumar'), '10000']
>>> tup1=tuple( emplstlst[0])
>>> tup1
('1', ('Arun', 'Kumar'), '10000')
>>> emplstlst[1][1]
('Bala', 'Mohan')
>>> emplstlst[1][1][1]
'Mohan'
>>> emplstlst[1][1][0]
'Bala'
>>> emplstlst[1][1][0]='Mohan'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> tup3=(emplstlst[1][1][1],emplstlst[1][1][0])
>>> tup3
('Mohan', 'Bala')
>>> tuple(tuple(emplstlst[0]),emplstlst[1])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: tuple expected at most 1 arguments, got 2
>>> tuple(emplstlst[0])
('1', ('Arun', 'Kumar'), '10000')
>>> tup3 = (tuple(emplstlst[0]),tuple(emplstlst[1]))
>>> tup3
(('1', ('Arun', 'Kumar'), '10000'), ('2', ('Bala', 'Mohan'), '12000'))
>>> emplstlst= [["1", ("Arun","Kumar"), "10000"],["2", ("Bala","Mohan"), "12000"
]]
>>> tsal =emplstlst[0][2] + emplstlst[1][2]
>>> tsal
'1000012000'
>>> tsal = int(emplstlst[0][2]) + int(emplstlst[1][2])
>>> tsal
22000

26. Write a program using for loop to print even numbers and odd numbers in the below range of data (generate using range function) [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] output should be with even as 6,8,10,12,14,16,18,20 and odd as 5,7,9,11,13,15,17,19.

lstrange =[5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in lstrange.range():
    print(i)
lstrange = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(lstrange)
lsteven = list()
lstodd = list()
for i in lstrange:
    if
i % 2 == 0:
lsteven.append(i)
else:
lstodd.append(i)

print(f"even nos list {lsteven}, odd nos list is {lstodd}")

27. Write a while loop to loop from 0 till 21 with the increment of 3, the result should be exactly 3,6,9,12,15,18 and store this result in a list

i=0
lst =list()
while i < 18:
    i=i+3
    lst.append(i)
print(lst)

#28. Write a for or while loop to print the cube of 4, result should be 4*4*4=64
# (initiate some variable outside the loop with 4 and loop through 3 times to achieve the result)

fourcube =4
i=1
while (i <=2):
    fourcube=fourcube*4
    print(fourcube)
    i=i+1
print(fourcube)

#29. Create a list as sal_lst=[10000,20000,30000,10000,15000], loop through the list and
# add 1000 bonus to the salary and store in another list sal_bonus_lst=[11000,21000,31000,11000,16000]
#then store the bonus applied salary in another list where sal>11000

sal_lst=[10000,20000,30000,10000,15000]
sal_gt10000 =list()
sal_bonus_lst=list()
for i in sal_lst:
    sal_bonus_lst.append(i+1000)
    if i > 11000:
        sal_gt10000.append(i)
print(sal_bonus_lst)
print(sal_gt10000)

#30. Write a do while loop to print “Inceptez technologies” n number of times as per the input you get from
# the user. Minimum it has to be printed at least one time regardless of the user input.

user_input = int(input())
i=1
while (True):
    print("Inceptez technologies")
    if i < user_input:
        i+=1
    else:
        break

#31. From the given list of list of elements produce the following output using nested for loop
#lst1=[[10,20],[30,40,50],[60,70,80]], calculate the sum of all number,
# calculate the min value and the max value of all the elements in the lst1.

lst1=[[10,20],[30,40,50],[60,70,80]]
total_sum =0
lst2 = list()
min,max=0,0
for i in lst1:
    for j in i:
        total_sum=total_sum+j
        lst2.append(j)
print(total_sum)
print(str(lst2.sort()))
print(f"min amount in list is {str(lst2[0])}, max amount in list is {lst2[lst2.__len__()-1]} ")

#32. Create a looping construct to create 3 tables upto 10 values. Output should be like this…
#1 x 3 = 3
#2 x 3 = 6
#10 x 3 = 30
i=1
while (i<=10):
    print(str(3),str('*'),i,"=",str(3*i))
    i+=1










