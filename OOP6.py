class Employee:
    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @fullname.setter
    def fullname(self, name): #后面的name是我们想要输入的值，比如下面的Jim Test
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Delete Name.')
        self.first = None
        self.last = None

emp_1 = Employee('Corey', 'Schafer')

emp_1.fullname = 'Jim Test'

print(emp_1.first)
print(emp_1.email) #()<parentheses.
print(emp_1.fullname)

del emp_1.fullname


