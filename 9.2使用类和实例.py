#9.2.1 CAR
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述信息"""
        long_name = str(self.year) + ' ' + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) +
              " miles on it.")

    def update_odometer(self, mileage):
        """
        将里程碑读数设置为指定的值
        禁止将里程表读数往回调
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")

    def increment_odometer(self, miles):
        """将里程表读数增加指定的量"""
        self.odometer_reading += miles

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_new_car.increment_odometer(100)
my_new_car.read_odometer()

#9-4
class Restaurant():

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_serve = 7

    def describe_restaurant(self):
        print("\nThe Restaurant's name is " +
              self.restaurant_name.title() + ".")
        print("Cuisine Type of the restaurant is: " +
              self.cuisine_type.upper() + ".")

    def open_restaurant(self):
        print("This Restaurant is Opening.")

    def read_number(self):
        print("This restaurant serves " +
              str(self.number_serve) + " people.")

    def set_number_served(self, mark):
        self.number_serve = mark

    def increment_number_served(self, add):
        self.number_serve += add



A = Restaurant('FS', 'ThaiFood')
A.describe_restaurant()
A.set_number_served(9)
A.increment_number_served(10)
A.read_number()

#9-5
class User():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name.title() + self.last_name.upper() +
        " is " + str(self.age) + " years old.")

    def greet_user(self):
        print("Hello! " + self.first_name.title() + "!")

    def increment_login_attemps(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def read_login_attempts(self):
        print("\nYou have tried to login for " +
              str(self.login_attempts) + " times.")

T = User('Chris', 'Chan', 23)
T.describe_user()
T.increment_login_attemps()
T.increment_login_attemps()
T.increment_login_attemps()
T.login_attempts = 7

T.read_login_attempts()

T.reset_login_attempts()
T.read_login_attempts()

