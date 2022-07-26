#สร้างฟังก์ชัน
from math import pi
def hello():
    print("Hello World")
    print("Khanisorn")
#เรียกใช้งานฟังก์ชัน
hello()
#ส่งค่าผ่านparameter
def sum(x,y):
    ans = x+y
    print(ans)
sum(5,8)
#ส่งค่าผ่านparameter+return
def sum(x,y):
    x+y
    return "Hi" 
print(sum(8,6))
