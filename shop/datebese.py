class Product:
    def __init__(self,brand,name,price,stock):
        self.brand = brand
        self.name = name
        self.__price = price
        self.__stock = stock

    def edit(self,val):
        if val == "editstock" :
            print('แก้ไขจำนวน')
            val_stock = int(input(f'{self.brand} ใส่จำนวน : '))
            self.__stock += val_stock
        
        elif val == "editprice":
            print('แก้ไขราคา')
            val_price = int(input(f'{self.brand} ใส่ราคา : '))
            self.__price = val_price

    def showinfo(self):
        return f"ชื่อแบรด์สินค้า: {self.brand} สินค้าชื่อ: {self.name} ราคา: {self.__price} บาท มีจำนวน: {self.__stock} ชิ้น"
    
class Mobile(Product):
    def __init__(self,brand, name, price, stock,system):
        super().__init__(brand,name, price, stock)
        self.system = system
    def showmobile(self):
        return f"{super().showinfo()}\nระบบปฏิบัติการ : {self.system}\n--------------------------------------------------------------------------------------"
    
class Notebook(Product):
    def __init__(self,brand, name, price, stock,ram):
        super().__init__(brand,name, price, stock)
        self.ram = ram
    def shownotebook(self):
        return f"{super().showinfo()}\nram : {self.ram}\n--------------------------------------------------------------------------------------"
    
class Cothes(Product):
    def __init__(self,brand,name, price, stock, Size):
        super().__init__(brand,name, price, stock)
        self.Size = Size
    def showclothes(self):
        return f"{super().showinfo()}\nไซส์ : {self.Size}\n--------------------------------------------------------------------------------------"
    
user01 = Mobile("Xiaomi","14 Ultra",35990,100,"Android")
user02 = Notebook("MSi","Titan 18 HX A14V",169990,20,"64GB (2x32GB) DDR5")
user03 = Cothes("Uniqlo","เสื้อฮู้ด ผ้าสเวต แบบสวมหัว ",1290,1200,"XS,S,M,L,XL,XXL,3XL")

while True:
    print(f"ข้อมูลของ{user01.showmobile()}")
    print(f"ข้อมูลของ{user02.shownotebook()}")
    print(f"ข้อมูลของ{user03.showclothes()}")
    choiec = input('จะแก้ไขข้อมูลพิมพ์ edit หรือ exit : ')
    if choiec == 'edit':
        user01.edit("editstock")
        user01.edit("editprice")
        user02.edit("editstock")
        user02.edit("editprice")
        user03.edit("editstock")
        user03.edit("editprice")
    elif choiec == 'exit':
        print(f"ข้อมูลของ{user01.showmobile()}")
        print(f"ข้อมูลของ{user02.shownotebook()}")
        print(f"ข้อมูลของ{user03.showclothes()}")
        break
    else:
        print('ลองใหม่อีกครั้ง')