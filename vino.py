#set> unoredered collections of data types,{}
mydate={"data","data1",0,1,0,"data2"}
print(mydate)
mydate.insert=(34.2)
print(mydate)
mydate.append("date")
print(mydate)
mydate[1]="date"
print(mydate)
del mydate
print(mydate)

#TUPLE
MYTUPLE=("DELL","LENEVO","ASUS",2373,78.98)
print(MYTUPLE)
print(len(MYTUPLE))
#update,insert,append,delete ,cannot work or not.
del MYTUPLE
print(MYTUPLE)

#dictionary
mydic={"brand":"hp",
       "color":"red", 
       "year":2022}
print(mydic)
mydic["color"]="blue"
print(mydic)
mydic["modelno"]=12345
print(mydic)
mydic["brand"]="asus","lenovo"
print(mydic)
del mydic["brand"]
print(mydic)

#function <a set of data will b executed whwnever its inviked or called
def add():
  for i in range(10):
    print("hello,world")
add()  



v=("hello,world")
print(v[10:0:-2])
print(v[0:-7:3])
print(v[-10:-1:2])

def cal():
  a = int(input("enter the no"))
  b = float(input("enter 2nd no"))
  print("sum of nos is =",(a+b))
cal()

def a(name):
  print("my name is ",name)
a("vinothkumar")
