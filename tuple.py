#ปริ้นจากหน้า
fruits = ("apple","banana","cherry")
print(fruits[1])
#ปริ้นจากหลัง
fruits = ("apple","banana","cherry")
print(fruits[-1])
#ปริ้นเป็นช่วง ถ้าไม่ใส่ค่าด้านหน้าจะปริ้นตั้งแต่คำแรก
fruits = ("apple","banana","cherry","orange","kiwi","melon","mango")
print(fruits[2:5])
print(fruits[2:])
print(fruits[:5])
#แทนที่ค่าในtuple 
x = ("apple","banana","cherry")
y = list(x) #ต้องแปลงเป็นlistก่อน แล้วเก็บเป็นค่าy
y[1] ="kiwi"
x = tuple(y) #แปลงเป็นlistกลับเป็นtuple แล้วเก็บเป็นค่าx
print(x)
#เพิ่มค่าในtuple 
x = ("apple","banana","cherry")
y = list(x)
y.append("orange")
x = tuple(y)
print(x)
#ลบค่า
x = ("apple","banana","cherry")
y = list(x)
y.remove("apple")
x = tuple(y)
print(x)
#่join tuple
tuple1 = ("a","b","c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
#นายคณิศร ริมแพร ม.6/14 เลขที่33