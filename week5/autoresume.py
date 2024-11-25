resume = {"Nickname":"","number":"","Hobby":"","color":""}
quantity = int(input("จำนวนค่าที่จะป้อน : "))
for i in range(1, quantity + 1):
    print(f"ข้อมูลคนที่ {i}")
    Playname = str(input("กรอกชื่อเล่น :"))
    resume["Nickname"] = Playname
    lagty = str(input("กรอกเลขที่ :"))
    resume["number"] = lagty
    Adelag = str(input("กรอกงานอดิเรก :"))
    resume["Hobby"] = Adelag
    Likecolor = str(input("กรอกสีที่ชอบ :"))
    resume["color"] = Likecolor
    print(resume)