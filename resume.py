name = str(input('กรอกชื่อ-สกุล '))
nickname = str(input('กรอกชื่อเล่น '))
age = int(input('กรอกอายุ '))
ID = int(input('กรอกรหัสประจำตัวนักศึกษา '))
level = int(input('กรอกระดับชั้น '))
height = float(input('กรอกส่วนสูง '))
weight = float(input('กรอกน้ำหนัก '))
result = height+weight
print("ชื่อ: "+name+" ชื่อเล่น: "+nickname)
print("อายุ: "+str(age)+" รหัสประจำตัวนักศึกษา: "+str(ID)+" ระดับชั้น: "+str(level))
print("ส่วนสูง: "+str(height)+" น้ำหนัก: "+str(weight))
print("ส่วนสูง + น้ำหนัก = "+str(result))

