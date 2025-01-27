class cat :
    def __init__(self,cat_name,cat_color):
        self.name = cat_name
        self.color = cat_color
    def cry(self):
        print(self.name,"เมี้ยวๆ")
mycat1 = cat("ศรีทอง","สีส้ม")
mycat2 = cat("ศรีเงิน","สีขาว")
mycat1.cry()
