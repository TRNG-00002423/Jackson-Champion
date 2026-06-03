class Employee:
    employee_count = 0
    company = "Revature"
    def __init__(self, name, role):
        Employee.employee_count += 1
        
        self.employee_id = Employee.employee_count
        self.name = name
        self.role = role
        

    def display_info(self):
        print(f"Employee Name: {self.name}, Employee Role: {self.role}")
        
    @classmethod
    def admin(cls, name):
        return cls(name, "admin")
    
    
emp1 = Employee("Oscar", "QA Engineer")
emp2 = Employee("Cody", "Software Engineer")
emp3 = Employee.admin("Jasdhir")
print(emp1.name)
print(emp2.name)
print(emp3.name)
print(emp3.role)

print(emp1.employee_id)
print(emp2.employee_id)
print(emp3.employee_id)
print(Employee.employee_count)
