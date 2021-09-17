# Instance variable: Datas are unique for each instance
# Class variable: variables(Datas) that are shared among all instances of a class
# Class method is declared by adding a decorator and uses a cls argument -> Usually to create an instance
# Static method doesn't have cls and self as arguments
# Special(magic/dunder) methods: __init__, __repr__, __str__, __add__, look at datetime module


class Employee:

    raiseAmount = 1.04  # class var
    numOfEmployees = 0

    def __init__(self, firstName, lastName, salary):
        self.firstName = firstName  # instance var
        self.lastName = lastName  # instance var
        self.salary = salary  # instance var
        self.email = '{}.{}@email.com'.format(self.firstName, self.lastName)

        Employee.numOfEmployees += 1  # class var

    @property
    def fullname(self):
        return '{} {}'.format(self.firstName, self.lastName)

    @fullname.setter
    def setfullname(self, name):
        first, last = name.split(" ")
        self.first = first
        self.last = last

    def raiseSalary(self):
        self.salary = int(self.salary * Employee.raiseAmount)

    @classmethod
    def setRaiseAmount(cls, amount):
        cls.raiseAmount = amount

    @classmethod
    def fromStringCreateEmployee(cls, string):
        first, last, pay = string.split('-')
        return cls(first, last, pay)

    @staticmethod
    def isWorkday(day):
        if day.weekday() == 6 or day.weekday() == 7:
            return False
        return True

    # Dunder methods
    # for debugging
    # def __repr__(self):
    #     return (f'{self.firstName}, {self.lastName} - , {self.salary}')

    # def __str__(self):
    #     return (f'{self.firstName} {self.lastName} - {self.email}')

    # def __add__(self, other):
    #     return self.salary + other.salary


class Developer(Employee):
    raiseAmount = 1.10

    def __init__(self, firstName, lastName, salary, progLanguage):
        super().__init__(firstName, lastName, salary)  # calling parent's constructor
        self.progLanguage = progLanguage
    pass


class Manager(Employee):
    raiseAmount = 1.15

    def __init__(self, firstName, lastName, salary, employees=None):
        super().__init__(firstName, lastName, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def addEmployee(self, employee):
        if employee not in self.employees:
            self.employees.append(employee)

    def removeEmployee(self, employee):
        if employee in self.employees:
            self.employees.remove(employee)

    def printAllEmployees(self):
        for employee in self.employees:
            print('-->', employee.printFullName())


manager1 = Manager('Nathaniel', 'Lee', 150000)
manager1.fullName = 'Binh Vo'  # calling setter method
print(manager1.fullName)  # calling getter method
# emp1 = Developer('Binh', 'Vo', 65000, 'Python')
# emp2 = Employee('Trash', 'Bin', 40000)

# manager1.addEmployee(emp1)
# manager1.addEmployee(emp2)
# print(manager1.email)
# manager1.printAllEmployees()

# # isinstance(), issubclass() - return a bool if a an instance is part of a particular class or subclass
# print(isinstance(emp1, Employee))
# print(issubclass(Manager, Developer))


# emp_str_3 = 'David-Lee-90000'
# emp3 = Employee.fromStringCreateEmployee(emp_str_3)
# print(emp3.__dict__)
# # print(help(Developer))
# Employee.setRaiseAmount(1.05)

# # Both ways are ==, Using an instance to call a method
# # Using a Class and pass in the instance for it to reference it-'self'
# print(emp1.printFullName())
# print(Employee.printFullName(emp1))
# print(emp2.__dict__) # Getting all attributes of an instance or a class

# import datetime
# day_off = datetime.date(2018, 8, 17)
# print(Employee.isWorkday(day_off))

# # Using Dunder Methods
# print(repr(emp1))
# print(str(manager1))
# print(emp1 + manager1)
