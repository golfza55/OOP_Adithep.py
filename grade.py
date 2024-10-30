score = int(input("ใส่คะแนน: "))
if score >= 100:
    print("มูฮ่าๆๆ")
elif score >= 80:
    print("คุณได้เกรด 4") 
elif score >= 70:
    print("คุณได้เกรด 3") 
elif score >= 60:
    print("คุณได้เกรด 2")
elif score >= 50:
    print("คุณได้เกรด 1")
elif score < 50:
    print("คุณได้เกรด 0 จะแก้ไหม")
    recovery = str(input("จะแก้ 0 ไหมจ๊ะ ตอบ แก้พิมพ์ Yes หรือ ไม่แก้พิมพ์ No: "))
    if recovery == "Yes":
        print("ดีมากๆครับ คุณขาดคะแนนอีก"+str(50-recovery)+"ถึงจะผ่าน")
    elif recovery == "No":
        print("ไม่ผ่านนะ")
else :
    print("กรอกตัวเลขใหม่")