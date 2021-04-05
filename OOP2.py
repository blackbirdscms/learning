class Employee:
    num_of_emps = 0
    raise_amount = 1.04

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
        # raise_amount是类变量，在上面。注意要加类的名称才能调用。
        # "Employee.raise_amount" = "self.raise_amount"
        # self.raise_amount可以在后面单独修改某一实例的倍率


print(Employee.num_of_emps)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

print(Employee.num_of_emps)

# instance variables-实例变量 & class variables-类变量
# num_of_emps是类变量，raise_amount是实例变量
