class Product:
    def __init__(self,name,price,stock):
        self.name = name
        self.__price = price
        self.__stock = stock
    def edit(self,val):
        if val == "stock" :
            print('แก้ไขจำนวน')
            val_stock = int(input('ใส่จำนวน'))
            self.__stock += val_stock
        elif val == "price":
            print('แก้ไขราคา')
            val_price = int(input('ใส่ราคา : '))
            self.__price = val_price
    def showinfo(self):
        return f"สินค้าชื่อ {self.name} ราคา {self.__price} บาท มีจำนวน {self.__stock} ชิ้น"
    
product1 = Product('ไอโฟน 15',3500,10)
product1.edit("stock")
product1.edit("price")
print(f"ข้อมูลของ{product1.showinfo()}")