a = 0
while True:
    try:
        pice = input("ใส่ค่า : ")
        if pice == "exit":
            print(f"ผลรวทคือ {a}")
            break
        pice = int(pice)
        if pice == 0:
            raise ZeroDivisionError
        elif pice < 0:
            raise Exception
        else:
            a += pice
            print(a)

    except ZeroDivisionError:
        print("ห้ามกรอก 0 ")
    except ValueError:
        print("ห้ามกรอกอย่างอื่นที่ไม่ใช่ตัวเลข")
    except:
        print("ห้ามกรอกค่าติดลบ")
    
    