# Public, Private and Protected Access specifiers

class Employee:
    no_of_leaves = 2
    _prot = 10
    __private = 12

    def __init__(self, aname, asalary, arole):
        self.salary = asalary
        self.name = aname
        self.role = arole

    def printDetails(self):
        return "Name is {}, salary is {} , role is {}".format(self.name, self.salary, self.role)

    @classmethod
    def change_leaves(cls,
                      newleaves):  # since it is a class method, no self will be there. we will work only on class
        # not object
        cls.no_of_leaves = newleaves

    @classmethod
    def from_str(cls, string):
        parms = string.split("-")
        return cls(parms[0], parms[1], parms[2])

    @staticmethod
    def print_good():
        print("This is a static method")
        return "hi"

emp = Employee("Riya", 100, "programmer")
print(emp._prot)
print(emp.__private)# name mangling will be done by python. to access it do emp._Employee__private