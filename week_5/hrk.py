money = [10,20,30]
#money.append(20)เพิ่มข้าโดยการต่อท้าย
#money.insert(2,25) ข้างหน้าคือ ตำแหน่งเริ่มนับจาก 0 ข้างหลังคือค่าที่จะเพิ่มเข้าไป
#del money[1]ลบค่า
while True:
    num = (int(input('หยอดเงินใส่กระปุก : ')))
    money.append(num)
    print(money)
    if num == 0:
        print(f"เงินเก็บทั้งหมด = {sum(money)}")
        break
