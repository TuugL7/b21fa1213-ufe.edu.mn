#1.Гараас оруулсан n тоо хүртэл “*” тэмдэгтийг мөр бүрд хэвлэх функц бич. 
def gg(n):
    for i in range(1, n + 1):
        print("*" * i)
        
n = int(input("n тоог оруулна уу: "))
gg(n)
#2.Гараас оруулсан n тоо хүртэл “*” тэмдэгтийг жагсаалтын мөр бүрд хэвлэх функц бич
#3 Багшаа энэ 3-р дасгал нь 2-тойгоо ижилхэн юмуу би ойлгодоггүй ээ.
#3.Дараах жагсаалтаас хамгийн их, хамгийн бага key-г авах функц бич.
import operator
students = {'Bat': 18,'Oyun': 22,'Dulam': 21,'Suren': 20}

a=max(students.items(), key=operator.itemgetter(1))[0]
b=min(students.items(), key=operator.itemgetter(1))[0]

print(f"Хамгийн их утга болон түүнээс хамгийн бага утга тэмдэгтүүр: {a} ба {b}")
#4.np.arange(1-1000) массив үүсгэ. Тухайн массиваас 3 эсвэл 7 –д хуваагдах тоонуудын нийлбэрийг ол.
import numpy as np
a=np.arange(1,1000)
b=0
for i in a:
    if i%7==0 or i%3==0:
        b+=i
print(b)