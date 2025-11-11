

# OO - features

# Abstraction
# Encapsulation
# Inheritance
# Polymorphism


class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def display(self):
        print ("Person:")
        
        print (f"{self.first_name} {self.last_name}")

class Employee(Person):
    def __init__(self, first_name, last_name, employee_id):
        super().__init__(first_name, last_name)
        self.employee_id = employee_id

    def display(self):
        print ("Employee:")
        
        # D.R.Y. - don't repeat yourself
        #print (f"{self.first_name} {self.last_name}")
        super().display()
       
        print (f"EmployeeId:{self.employee_id}")

e = Employee("Alice", "Adams", "E12345")
e.display()

#print (e.employee_id)


