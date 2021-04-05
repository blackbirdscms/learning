class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + ' ' + last + '@company.com'

        Employee.num_of_emps += 1  # 每新建一个员工，员工数量就增加1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str): #替代构造函数
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay) #这行代码将创建并返回新员工

    @staticmethod
    def is_workday(day): #it does not take anything as first argument
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

import datetime
my_date = datetime.date(2016, 7 ,10)
print(Employee.is_workday(my_date)) #检测是否工作日

Employee.set_raise_amt(1.05)

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

emp_str_1 = 'john-doe-70000'
emp_str_2 = 'steve-smith-30000'
emp_str_3 = 'jane-doe-90000'

#first, last, pay = emp_str_1.split('-') #使用split分开字符串

new_emp_1 = Employee.from_string(emp_str_1)
 #alternative constructor 替代构造函数


print(new_emp_1.email)
print(new_emp_1.pay)

