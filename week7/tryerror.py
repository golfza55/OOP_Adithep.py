try:
    sum = int(input("ใส่ยอดซื้อ : "))
    if sum == 0:
        raise ZeroDivisionError
    elif sum < 0:
        raise Exception
    elif sum >= 5000:
        total = sum * 0.2
        print(f"ส่วนลดราคาสินค้า {total} บาท")
        print(f"ราคาสุทธิ {sum - total}")
    elif sum >= 2000:
        total = sum * 0.1
        print(f"ส่วนลดราคาสินค้า {total} บาท")
        print(f"ราคาสุทธิ {sum - total}")
    elif sum == 4999:
        total = sum * 0.1
        print(f"ส่วนลดราคาสินค้า {total} บาท")
        print(f"ราคาสุทธิ {sum - total}")
    else:
        print("ไม่ได้รับส่วนลด")
except ValueError:
    print("ใส่เฉพาะตัวเลข")
except ZeroDivisionError:
    print("ห้ามใส่ 0")
except:
        print("ห้ามใส่เลขติดลบ")