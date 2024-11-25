class Gun:
    def __init__(self,name,ammo,Blood):
        self.name = name
        self.กระสูน = ammo
        self.พลังชีวิต = Blood
    def add_ammo(self,ammo):
        self.กระสูน += ammo
    def tir_ammo(self):
        if self.กระสูน > 0 :
            self.กระสูน -= 1
        else:
            print('กระสุนหมด')
    def fire_gun(self,enemy):
        self.กระสูน -=1
        enemy.พลังชีวิต -=3

gun1 = Gun("t1",5,10)
gun2 = Gun("t2",10,5)
gun1.fire_gun(gun2)
print(gun1.กระสูน)
print(gun2.พลังชีวิต)