#1. ให้เขียนโปรแกรมรับค่าตัวเลข 2 ตัวและแสดงผลจากตัวแรกจนถึงตัวสุดท้ายแต่ให้ข้ามตัวเลขที่หาร 3 ลงตัว(เช่น 3, 6, 9) โดยใช้คำสั่ง for loop
def number(num1,num2): 
    funtion1 = []
    for i in range(num1,num2+1):
        if  i % 3 !=0:
            funtion1.append(i)
    return funtion1