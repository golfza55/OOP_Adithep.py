class student :
    def __init__(self, name ,id ,age):
        self.name = name
        self.id = id
        self.age = age
        self.grader = {}
    def score(self):
        choice = input('กรุณาเลือกวิชาที่จะกรอกคะแนน : ')
        score = int(input('.ใส่คะแนน :'))
        grade = self.grader(score)
        if choice == "M":
           self.grader["Math"] = grade
        elif choice == "T":
           self.grader["Thai"] = grade 
        elif choice == "S":
           self.grader["Science"] = grade
    def geader(slef,score):
        if score >= 80 :
            return 4
        if score >= 70 :
            return 3
        if score >= 60 :
            return 2
        if score >= 50 :
            return 1
        else:
            return 0

stu1 = student("soph",1)
stu2 = student("bob",2)
print(stu2.id)