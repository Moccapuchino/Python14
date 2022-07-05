#แสดงค่า
fruits = ["apple","banana","cherry",]
print(fruits[0])
#เปลี่ยนค่า
fruits[0] ="blackcurrant"
print(fruits[0])
fruits[0:2] = ["mango","watermelon"]
print(fruits)
#เพิ่มค่า
fruits.append("raspberry")
print(fruits)
#เพิ่มในที่กำหนด
fruits.insert(2,"grape")
print(fruits)
tropical=("papaya","pineapple")
fruits.extend(tropical)
print(fruits)
#ลดค่า
fruits.remove("grape")
print(fruits)
fruits.pop(0)
print(fruits)
#del fruits
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
#นายคณิศร ริมแพร ม.6/14 เลขที่33