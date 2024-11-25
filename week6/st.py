import random
class Student:
    def __init__(self,name,nickname,score):
        self.name = name
        self.nickname = nickname
        self.score = score
    def random(self):
        a = random.randint(0,10)
        self.score += a
    def std_score(self):
        if self.score > 5:
            print('คุณสอบผ่าน')
            print('----------')
        else:
            print('คุณสอบตก')
            print('----------')

student1 = Student(name="มฤคินทร์",nickname="มิกซ์",score=0)
student2 = Student(name ="อดิเทพ",nickname="กอล์ฟ",score=0)
student3 = Student(name="วชิรวิชญ์",nickname="ปอน",score=0)
student4 = Student(name="โยธินันท์",nickname="ก้อง",score=0)
student5 = Student(name="ภูริภัทร",nickname="ภู",score=0)
student1.random()
student2.random()
student3.random()
student4.random()
student5.random()
print(f"{student1.name} สอบได้ {student1.score} คะแนน ")
student1.std_score()
print(f"{student2.name} สอบได้ {student2.score} คะแนน ")
student2.std_score()
print(f"{student3.name} สอบได้ {student3.score} คะแนน ")
student3.std_score()
print(f"{student4.name} สอบได้ {student4.score} คะแนน ")
student4.std_score()
print(f"{student5.name} สอบได้ {student5.score} คะแนน ")
student5.std_score()