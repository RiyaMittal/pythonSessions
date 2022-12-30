class Employee:
    no_of_leaves = 10

    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def printDetails(self):
        return "my name is {}, salary is {}, role is {}".format(self.name, self.salary, self.role)

    @classmethod
    def change_leaves(cls, leaves):
        cls.no_of_leaves = leaves

    @staticmethod
    def from_str():
        print("Hi I am static")

    # def __add__(self, other):
    #     return self.salary + other.salary

    # def __repr__(self):
    #     return "Employee({self.name},{self.salary},{self.role})".format(self.name, self.salary, self.role)

    # def __str__(self):
    #     return "my name is {}, salary is {}, role is {}".format(self.name, self.salary, self.role)


riya = Employee("RIYA", 200, "Instr")
jothi = Employee("JOTHI", 500, "Stu")

# print(riya+jothi) # use dunder add method

# repr , str
# print(riya)

# if we str alsom then it will always call str not repr, you have to specifically call repr. if str is not there then repr,

# print(repr(riya))