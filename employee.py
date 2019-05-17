class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
    
    @property
    def email(self):
        return '{}.{}email.com'.format(self.first,self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self,name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{}-{}'.format(self.fullname, self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname)

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        Employee.__init__(self, first, last, pay)
        #in python3, we can simply use super().__init__(first,last,pay)
        #but in python2.7, we need to use parent class.__init__(self, ...)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        Employee.__init__(self, first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    
    def remove(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname)


# print(help(Developer))

# print(dev_1.email)
# dev_1.apply_raise()
# print(dev_1.prog_lang)
# print(type(Employee))
# mgr1.print_emps()
# mgr1.add_emp(dev_2)
# mgr1.print_emps()

# print(isinstance(mgr1, Manager))
# print(isinstance(mgr1, Employee))
# print(issubclass(Developer, Employee))
# print(issubclass(Manager, Employee))




emp_1 = Employee('Corey', 'Schafer', 50000)
emp_1.first = 'Jim'
emp_2 = Employee('emp2', 'emp2last', 60000)

# dev_1 = Developer('Test', 'Employer', 60000, 'java')
# mgr1 = Manager('Sue', 'Smith', 90000, [dev_1])
# # print(mgr1.email)
# print(emp_1)
# print(emp_1.__repr__())
# print(emp_1.__str__())

#downder
#print(1+2) ==
# print(int.__add__(1,2))
# # print('a' + 'b') ==
# print(str.__add__('a', 'b'))
# print(emp_1 + emp_2)
# print('test'.__len__())
# print(len(emp_1))

emp_1.fullname = 'Jim Smith'
# print(emp_1.first)

print(emp_1.fullname)
del emp_1.fullname
