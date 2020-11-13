
class Dog():
    '''一次模拟小狗'''

    def __init__(self, name, age):
        '''每当创建新实例时候，python会自动运行
            self是一个指向实例本身的引用
            每一个类方法都有指向
        '''
        self.name = name;
        self.age = age;

    def sit(self):
        '''叫小狗蹲下'''
        print(self.name + " is sitting")

    def roll_over(self):
        '''叫小狗打滚'''
        print(self.name + " is rolling")


d1 = Dog("will", 6)
print("name:" + d1.name + " age:" + str(d1.age))

d1.sit()
d1.roll_over()


#继承

class Car():
    def __init__(self,make,model,year):
        self.make=make;
        self.model=model;
        self.year=year;
        self.odometer_reading = 0

    def get_description(self):
        '''获取车辆描述'''
        long_name = str(self.year)+" " +self.make +" "+self.model
        return long_name.title()

    def fill_gas_tank(self):
        '''加油'''
        print("gas tank filled")

class ElectricCar(Car):
    '''电动汽车'''

    def __init__(self,make,model,year):
        '''添加电动汽车特有属性：电池容量'''
        super().__init__(make,model,year)
        self.battery_size = 100

    def describe_battery(self):
        print("This car has a "+str(self.battery_size)+"-kwh battery")

    def fill_gas_tank(self):
        '''电车加不了油'''
        print("ElectricCar has no gas tank")



car = Car("tesla","model s",2006)
tesla = ElectricCar("tesla","model s",2006)
print(tesla.get_description())
tesla.describe_battery()

car.fill_gas_tank()
tesla.fill_gas_tank()
