'''
name="abhishek"
for names in name:
    print(names)


for i in range(5,25,5):
    print("printing",i) 
print("loop ended")

a= [10,40,'Abhishek', 5.6]
for item in a:
    print(item, end=" ")

for i in range(5):
    print("the outer loop",i)
    for j in range(3):

        print(" the inner loop",j)

print("loop ended")


data=[1,45,57]
print(data)
data.append(100)
data.append("python")
data.insert(2,"abhishek")
print(data)

mix_lst=[{'key1':"value1"}, [10,20,30], (5,6,7)]
tup=(1,2,3,4)
mix_lst.append(tup)
print(mix_lst)

num=int(input("enter a number"))
while num<50:
    print("the number is",num)1
    num+=10
    #num2=int(input("enter a number"))
    #while num2<30:
        #print("the number is less than 30",num)
        #break
print("loop ended")



#t("loop ended")

#muliplication table of a number
num=int(input("enter a number"))
count=1
while count<=10:
    product= num * count
    print(f"{num} x {count} = {product}")
    count+=1

color=['red', 'green', 'blue']
for i in color:
    print(i)

data=[1,2,3,4,5]
data.append(6)
data.append("abhishek")
print(data)


data=[10,20,30,40]
data2=data.copy()
print(data2)


T=1,2,3,'ram',
print(T)
list=list(T)
print(list)
list.append('shyam')
T2=tuple(list)
print(T2)




data=(4,45,67,89)
list_data=list(data)
print(type(list_data))
print(list_data)
list_data.append("abhishek  ")
print(list_data)
tupple_data=tuple(list_data)
print(tupple_data)

#set operations
data={1,2,3,4,5}
#data2={3,4,5,6,7}
data2=data.copy()
print(data2) #set() empty set 
            #{} empty dictionary

set1={ 12,45,78}
set2={45,0,7}
print(set1.update(set2))
#set3=set1+set2

1#python history/compiler/interpreter #types of lamguage
2#variable naming conventions #data types
3#type  casting / input / keyworda  
4#operators
5# condtional statements
6# loops
7# data structures

#dictinoary operations
data={'name':"abhishek", 'age':24, 'city':"pune"}
print(data)
for i in data:
    print(i) #key 
for va in data.values():
    print(va) # values

for name in data.items():
    print(name) # key , value pairs


dict={}
dict['name']="abhishek"
dict['age']=24
print(dict)
dict2={"place":"pune", "course":"python"}
dict.update(dict2)
print(dict['place'])
dict.clear()
print(dict)


#function operations
def greet(): #parameter
    print("hello abhishek")
    print("welcome to python programming")  
greet() #arguments 

def add_numbers(num1, num2): #parameters
    pass
    


#calling function with arguments
#def joding(y):
    #x=10
    #result=x+y
    #print("the result is", result)
#joding(5) #arguments


#variable lenghth arguments
def show(*nums):
    z=nums[0]+ nums[1]+ nums[2]
    print("the total is",z)
show(10,20,30)

#add to num using function

 
a=10
b=20
mean=(a+b)/2
print("the mean is", mean)

c=30
d=40
mean2=(c+d)/2
print("the mean is", mean2)

def malai_yaha_mean(num1, num2):
    mean=(num1+num2)/2
    print("the mean is", mean)
malai_yaha_mean(10,20)
malai_yaha_mean(30,40)
malai_yaha_mean(50,60)
malai_yaha_mean(70,80)

def seeme():
    x=10
    y=20
    seeme=x+y
    print("the total is", seeme)
seeme()

#paramter
def add(second):
    first=10
    total= first + second
    print("the total is", total)
add(60) 
add(90)

#positional arguments
def pag(name,place="Kathmandu"):
    
    print(f"hello my name is  {name}, welcome to {place}")
pag("ashok") #default arguments

#varibale length arguments
def show(*nums):
    z=nums[1]* nums[1]+ nums[1]* nums[2]
    print("the total is",z)
show(10,20,30)

#keyword variable length arguments
def display(**info):
    print("the name is", info['name'])
    print("the age is", info['age'])
display(name="abhishek", age=24)

#returning values from function
def malaiyokurapaxigarnuxa(ahile, thaxaina):
    
    
    pass

#hash function
def hash_function(data):
    return hash(data)
result=hash_function("0")
print("the hash value is", result)



#global variable
x=4
print(x)

def show():
    x=5
    print(f'the local x is {x} ')
    print("hello world")
print(f'the global x is outside function {x} ')
show()
print(f'the global x is {x} ')

x=10
def func():
    global x
    x=15
    print(f'the local x is {x} ')
    print("hello world")
func()
print(x)

#
y=20
def outer():
    z=30
    def inner():
        a=40  
        nonlocal z
        z=z+10
        print(f'the innner a is {a} ')
        print(f'the inner z is {z} ')
        print(f'the inner y is {y} ')
    inner()
    print(f'the outer z is {z} ')
outer()

#global , nonlocal variable
a=5
def outer_function():
    b=10
    print(a)
    print(f'the outer b is {b} ')
#print("b:",b)   #error b is not defined
outer_function()
print("a:",a)

#lamda function
add=lambda x,y: (x+y, x-y )

a,b=add(5,10)
print("the addition is",a)
print("the subtraction is",b)

#map function with lambda
li=[1,2,3,4,5]
squared=map(lambda x: x**2, li)
print("the squared values are", squared)

#filter function with lambda
numbers=[10,15,20,25,30,35]
even_numbers=filter(lambda x: x%2==0, numbers)
print("the even numbers are", list(even_numbers))



a=10 #global variable
def outer():
    x=40 #enclosing variable
    def inner():
        y=50 #local variable
        #global a
        #a=a+10
        nonlocal x
        x=x+40 #80
        print(f"this is inner function{x} and {y} and {a}") #a=20
    inner()
    print(f"this is outer function{x} and {a}") #a=20
print("rhis is outer function")   
outer()
print("end of program")
#inner()  #error inner() is not defined

#lamda
#sum=lambda x,y,z: x+y+z, x-y-z, x*y*z
#sum(10,20, 50)
#print("the sum is", sum(10,20,50)(0,1,3))

#map function
numbers=2,3,4,5
cube=map(lambda x: x*x*x, numbers)
print("the squared values are", list(cube))

#filter function
values=[10,15,22,33,40,55,60,0,2,5,75,80,90,100]
even_numbers=filter(lambda x: x%2==0, values)
print("the even numbers are", list(even_numbers))

#reduce function
from functools import reduce
data=[1,2,3,4,5] 
sum=reduce(lambda x,y: x+y, data)
print("the total sum is", sum)



#file handeling
#reading files
file =open("note.txt","r")
content=file.read()
print(content)
file.close()

#read line by line
file=open("note.txt","r")
for line in file:
    print(line.strip())
file.close()

#specific number of characters
file=open("note.txt","r")
print(file.read(10))
file.close()

#writing to a file 'w' mode
file=open("notes2.txt","w")
file.write("hello everyone welcome to python programming\n")
file.write("this is boring class\n")
file.close()

#write line
file=open("myfile.txt", 'w')
lines=["hello class\n", "welcome to this online lecture\n","have a great day"]
file.writelines(lines)
file.close()

f= open("myfile.txt", 'w')
lines=["This is first line", "This is second line", "This is third line"]
for line in lines:
    f.write(line+'\n')
f.close()


#readlines() function
file=open("marks.txt","r")
i=0
while True:
    i=i+1
    line=file.readline()
    if not line:
        break
    m1=int(line.split(",")[0])
    m2=int(line.split(",")[1])
    m3=int(line.split(",")[2])
    m4=int(line.split(",")[3])
    total= int(m1)+ int(m2)+ int(m3)+ int(m4)

    print(f"Marks for student {i} in maths is {m1}, science is {m2}, english is {m3}, computer is {m4} and total is {total}")
file.close()

#appending to a file 'a' mode
file=open("add.txt","a")
file.write("this is appended line 1\n")
file.write("yo chai maile lekhe ko ho\n")
file.write("yo chai arko line\n")
file.close()

file=open("add.txt","a")
file.write("this is another appended line\n")
file.close()


#with statement
with open("note.txt","r") as file:
    content=file.read()
    print(content)

#os
import os
os.rename("add.txt","added.txt")
os.remove("added.txt")
if os.path.exists("added.txt"):
    print("file exists")
else:
    print("file does not exist")


#copy content from one file to another
with open("note.txt","r") as source_file:
    content=source_file.read()

with open("notes2.txt","w") as dest_file:
    dest_file.write(content)

print("file copied successfully")


#count lines, words, characters in a file
with open("note.txt","r") as file:
    lines=file.readlines()
    num_lines=len(lines)
    num_words=sum(len(line.split()) for line in lines)
    num_characters=sum(len(line) for line in lines)

    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")
    print(f"Number of characters: {num_characters}")

    

#tell function
with open("tell.txt","r") as file:
    #print(file.tell())
    file.read(7)
    print(file.tell())

#seek function
with open("tell.txt","r") as file:
    file.read(2)
    print("current position:", file.tell())
    file.seek(1)
    print("after seeking to beginning:", file.tell())
    #content=file.read()
    #print(content)

with open("tell.txt","r") as file:
    print("line 1:", file.readline())

    file.seek(0)
    content=file.read()
    print("full content:", content.split("\n")[5])

#binary mode using seek
with open("git.jpg",'rb') as file:
    file.seek(10)
    print(file.tell())

#read file from middle
with open("mid.txt","r") as file:
    midpoint=len(file.read())//2
    file.seek(midpoint)
    print(file.read())


#pickle fucntion
import pickle
#data=['abhishek', 24, 'pune']
with open ("data.pkl","rb") as abhi:
    loaded_data=pickle.load(abhi)

print("the loaded data is", loaded_data)

#print("data serialized successfully")


import pickle
class person:
    def __init__(self, name, age, city):
        self.name=name
        self.age=age
        self.city =city

#p1=person("Ram",100,"aayodhya")
#p2=person("sita",60, "janakpur")
#p3=person("lakshman",90,"aayodhya")
import pickle
with open("person.pkl","rb") as persons:
    object=pickle.load(persons)
    
print("the name is", object.name)
print("the age is", object.age)
print("the city is", object.city)

    #pickle.dump(p1, address) 
    #pickle.dump(p2, address)
    #pickle.dump(p3, address)#


student= {
    "name":"abhishek",
    "age":24,
    "city":"kathmandu",
    "skills":["python","java"]
}
with open("self.pkl","wb") as selffile:
    pickle.dump(student, selffile)

print("data serialized successfully")

#dump & dumps
data= [1,2,3,4,5]

byte_data =pickle.dumps(data)
original=pickle.loads(byte_data)
print("the byte data is", byte_data)
print("the original data is", original )


# example using load loads dump and dumps
import pickle as pk
student={
    "name":"Abhishek",
    "age":24,
    "city":"kathmandu",
    "skills":["python","java"]
}
#dumps()
byte_data=pk.dumps(student)
print("byte data is", byte_data )

#loads()
print("from bytes: ")
pk.loads(byte_data)

#dump()
with open("class.pkl","wb") as classfile:
    pk.dump(student, classfile)

#load()
with open("class.pkl","rb") as classfile:
    loaded_data=pk.load(classfile)
    print("the loaded data is", loaded_data)

#oop- Object-Oriented Programming
#class done
#object done
#Encapsulation done
#Inheritance -types  done
#int() method __int__ done
#instance variable  done
#class variable done
#function inside class- method done
#polymorphism done
#Abstraction done

class Parent:
    def show(self):
        return "I am Parent"

class Child(Parent):
    def show(self):
        return "I am Child (Overridden)"

obj = Child()
print(obj.show())


#OOP 
class Car:
    brand="Tesla"
    Colo="black"

print("the car brand is", Car.brand)

#function in a class

class Subject:
    def __init__(self,name,code): #constructor
        self.name= name
        self.code= code 
subject1= Subject("maths",101)
print("the subject name is", subject1.name)
print("the subject code is", subject1.code)
    
#instance variable --> unique for each object
#class variable --> common among all objects
class Dog:
    species="Bull dog"  #class variable

    def __init__(self,name):
        self.name=name #instance varibale

dog1=Dog("tommy")
dog2=Dog("bruno")

print("dog1 name is", dog1.name)
print("dog2 name is", dog2.name)
print("dog1 species is", dog1.species)
print("dog2 species is", dog2.species)

#inheritance
class MithilaArt:
    def __init__(self):
        self.style = "Traditional"
        self.color = ["red", "yellow", "green", "blue"]

    def show_info(self):
        return f"style: {self.style}, colors: {self.color}"
        
class MadhubaniArt(MithilaArt):
    def __init__(self):
        super().__init__()    # Inheritance parent's class constructor
        self.border_design = "Double line Geometric border"

    def show(self):
        return f"Border Design: {self.border_design}"

if __name__ == "__main__":
    art = MadhubaniArt()  # Creating object of child class
    print(art.show_info())  # Accessing inherited method
    print(art.show())  # Accessing child class method

        
#style: Traditonal Mithila Style
#Color ""
#Boder: Doub   

#multiple inheritance
class GrandParent:
    def property(self):
        return "5 bigha land at Janakpur"

class Father(GrandParent):
    def house(self):
        return "3 BHK house at Kathmandu"

class Abhishek(Father):
    def bike(self):
        return "java"

obj=Abhishek()
print(obj.property())
'''
#polymorphism
class MomoSeller:
    def call_customers(self):
        return "yaha mitho momo painxa aaunus aaunus" 

class PanipuriWala:
    def call_customers(self):
        return "haina yaha aaunus yaha mittho chatpato panipuri painxa aaunus aaunus"

class Puriwala:
    def call_customers(self):
        return "aaunus aaunus yaha puri r sabji mittho cha"
    
for i in [MomoSeller(), PanipuriWala(), Puriwala()]:
    print(i.call_customers())



#Encapsulation
class InstaAccount:
    def __init__(self, username):
        self.username=username
        self.__private_message= ["this is private message"]  #private data

    def add_message(self, msg):
        self.__private_message.append(msg)  #private data

    def show_message(self):
        return self.__private_message #controlled access
acc=InstaAccount("abhishek")
acc.add_message("Hey bro whatuppp!!")
print(acc.show_message()) #allowed

#Abstraction
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod   # user-visible method is `pay`, subclasses implement it
    def pay(self):
        pass
   
class Esewa(Payment):
    def pay(self):
        return "Processing payment through Esewa"

class Khalti(Payment):
    def pay(self):
        return "Processing payment through Khalti"

class FonePay(Payment):
    def pay(self):
        return "Processing payment through FonePay"
    
paymentt=FonePay()
print(paymentt.pay())




#overrriding
class Parent:
    def rules(self):
        return "use phone for 1 hours."

class Child(Parent):
    def rules(self): #Overriding parent's method
        return " haina haina Ma chai 4 ghanta reels hererw basxu"

obj= Child()
print(obj.rules())


#Composition (HAS-A)

#youtuber xa and wu sang k k hunxa?
#1 camera
#2 Microphone
#3 Editor
#4 Content creator/ Script writer

#---> Camera 
class Camera:
    def record(self):
        return "Recording video in 4K"
    
class YouTuber:
    def __init__(self):
        self.camera= Camera()  # Composition (HAS-A)---> youtuber has a camera 
    
    def create_content(self):
        return self.camera.record() + " and editing the video"
    
yt_vid=YouTuber()
print(yt_vid.create_content())
