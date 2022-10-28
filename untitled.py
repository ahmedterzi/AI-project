class Faction:
    def __init__(self, name, num_of_units, h_point,attack_point, u_reg_num):
        self.name = name
        self.num_of_units = num_of_units
        self.h_point = h_point
        self.attack_point = attack_point
        self.u_reg_num = u_reg_num
        self.tot_health = self.num_of_units * self.h_point
        self.is_alive = True
    @staticmethod
    def AssgnEnemies(f_enemy, s_enemy):
        return f_enemy, s_enemy
    def PerformAttack(self, attack_point):
        if f_enemy.is_alive ==True and s_enemy.is_alive == True:
            f_enemy.ReceiveAttack(self, (self.attack_point/10)*5)
            s_enemy.ReceiveAttack(self, (self.attack_point/10)*5)
        elif f_enemy.is_alive ==True and s_enemy.is_alive == False:
            f_enemy.ReceiveAttack(self, self.attack_point)
        elif f_enemy.is_alive ==False and s_enemy.is_alive == True:
            s_enemy.ReceiveAttack(self, self.attack_point)
        else:
            pass
    def ReceiveAttack(self, enemy, point):
        if enemy == f_enemy:
            point = point
        else:
            point = point
        if self.tot_health <= 0:
            self.is_alive = False
        elif point > self.tot_health:
            self.tot_health = self.tot_health -point
            self.is_alive = False
        else:
            self.tot_health = self.tot_health -point
        self.num_of_units = self.tot_health / self.h_point
    def PurchaseWeapons(self, point_wanted, merchant):
        self.attack_point += point_wanted
        merchant.revenue += point_wanted
        merchant.weapon_point -= point_wanted
    def PurchaseArmors(self, point_wanted, merchant):
        self.h_point += point_wanted
        merchant.revenue += point_wanted
        merchant.weapon_point -= point_wanted
    def Print(self):
        return self.__dict__
    def EndTurn(self):
        if self.num_of_units <= 0:
            self.num_of_units = 0
            self.is_alive = False
        else:
            pass
        self.num_of_units += self.u_reg_num
        self.tot_health = self.num_of_units * self.h_point
    
class Merchant:
    def __init__(self, starting_weapon_point, starting_armor_point):
        self.weapon_point = starting_weapon_point
        self.armor_point = starting_armor_point
        self.revenue = 0
    def AssgnFactions(self,first_faction, second_faction, third_faction):
        self.first_faction = first_faction
        self.second_faction = second_faction
        self.third_faction = third_faction
    def SellWeapons(self, faction, point_wanted):
        if faction.is_alive == False:
            print('The faction you want to sell weapons is dead!')
        else:
            if point_wanted <= self.weapon_point:
                self.weapon_point -= point_wanted
                faction.PurchaseWeapons(point_wanted, self) 
            else:
                print('You try to sell more weapons than you have in possession.')
    def SellArmors(self, faction, point_wanted):
        if faction.is_alive == False:
            print('The faction you want to sell armors is dead!')
        else:
            if point_wanted <= self.armor_point:
                self.armor_point -= point_wanted
                faction.PurchaseArmors(point_wanted, self) 
            else:
                print('You try to sell more armors than you have in possession.')
    def EndTurn(self):
        self.weapon_point = starting_weapon_point
        self.armor_point = starting_armor_point

        
        
class Orcs(Faction):
    def __init__(self, name, num_of_units, h_point,attack_point, u_reg_num):
        super().__init__(name, num_of_units, h_point,attack_point, u_reg_num)
    def PerformAttack(self, attack_point):
        if f_enemy.is_alive ==True and s_enemy.is_alive == True:
            f_enemy.ReceiveAttack(self, (self.attack_point/10)*7)
            s_enemy.ReceiveAttack(self, (self.attack_point/10)*3)
        elif f_enemy.is_alive ==True and s_enemy.is_alive == False:
            f_enemy.ReceiveAttack(self, self.attack_point)
        elif f_enemy.is_alive ==False and s_enemy.is_alive == True:
            s_enemy.ReceiveAttack(self, self.attack_point)
        else:
            pass
    def ReceiveAttack(self, enemy, point):
        if enemy == f_enemy:
            point = point*3/4
        else:
            point = point*4
        if self.tot_health <= 0:
            self.is_alive = False
        elif point > self.tot_health:
            self.tot_health = self.tot_health -point
            self.is_alive = False
        else:
            self.tot_health = self.tot_health -point
        self.num_of_units = self.tot_health / self.h_point
    def PurchaseWeapons(self, point_wanted, merchant):
        self.attack_point += 2 * point_wanted
        merchant.revenue += 20 * point_wanted
        merchant.weapon_point -= point_wanted
    def PurchaseArmors(self, point_wanted, merchant):
        self.h_point += 3 * point_wanted
        merchant.revenue +=  point_wanted
        merchant.weapon_point -= point_wanted
    def Print(self):
        return self.__dict__
        
        
class Elves(Faction):
    def __init__(self, name, num_of_units, h_point,attack_point, u_reg_num):
        super().__init__(name, num_of_units, h_point,attack_point, u_reg_num)
    def PerformAttack(self, attack_point):
        if f_enemy.is_alive ==True and s_enemy.is_alive == True:
            f_enemy.ReceiveAttack(self, (self.attack_point/10)*4)
            s_enemy.ReceiveAttack(self, (self.attack_point/10)*9)
        elif f_enemy.is_alive ==True and s_enemy.is_alive == False:
            f_enemy.ReceiveAttack(self, self.attack_point)
        elif f_enemy.is_alive ==False and s_enemy.is_alive == True:
            s_enemy.ReceiveAttack(self, self.attack_point*3/2)
        else:
            pass
    def ReceiveAttack(self, enemy, point):
        if enemy == f_enemy:
            point = point*6/5
        else:
            point = point*3/4
        if self.tot_health <= 0:
            self.is_alive = False
        elif point > self.tot_health:
            self.tot_health = self.tot_health -point
            self.is_alive = False
        else:
            self.tot_health = self.tot_health -point
        self.num_of_units = self.tot_health / self.h_point
    def PurchaseWeapons(self, point_wanted, merchant):
        self.attack_point += 2 * point_wanted
        merchant.revenue += 15 * point_wanted
        merchant.weapon_point -= point_wanted
    def PurchaseArmors(self, point_wanted, merchant):
        self.h_point += 4 * point_wanted
        merchant.revenue +=  5 * point_wanted
        merchant.weapon_point -= point_wanted
    def Print(self):
        return self.__dict__
    
    
    
class Dwarwes(Faction):
    def __init__(self, name, num_of_units, h_point,attack_point, u_reg_num):
        super().__init__(name, num_of_units, h_point,attack_point, u_reg_num)
    def PerformAttack(self, attack_point):
        if f_enemy.is_alive ==True and s_enemy.is_alive == True:
            f_enemy.ReceiveAttack(self, (self.attack_point/10)*5)
            s_enemy.ReceiveAttack(self, (self.attack_point/10)*5)
        elif f_enemy.is_alive ==True and s_enemy.is_alive == False:
            f_enemy.ReceiveAttack(self, self.attack_point)
        elif f_enemy.is_alive ==False and s_enemy.is_alive == True:
            s_enemy.ReceiveAttack(self, self.attack_point)
        else:
            pass
    def ReceiveAttack(self, enemy, point):
        if enemy == f_enemy:
            point = point
        else:
            point = point
        if self.tot_health <= 0:
            self.is_alive = False
        elif point > self.tot_health:
            self.tot_health = self.tot_health -point
            self.is_alive = False
        else:
            self.tot_health = self.tot_health -point
        self.num_of_units = self.tot_health / self.h_point
    def PurchaseWeapons(self, point_wanted, merchant):
        self.attack_point += point_wanted
        merchant.revenue += 10 * point_wanted
        merchant.weapon_point -= point_wanted
    def PurchaseArmors(self, point_wanted, merchant):
        self.h_point += 2 * point_wanted
        merchant.revenue +=  3 * point_wanted
        merchant.weapon_point -= point_wanted
    def Print(self):
        return self.__dict__
        
        
