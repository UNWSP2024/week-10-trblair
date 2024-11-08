# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.

# Once you have written the class, write a program that creates three Employee objects to hold the following data.

# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.
class Employee:
    def __init__(self,name,ID,Department,Title):
        self.name=name
        self.ID=ID
        self.Department=Department
        self.Title=Title

employee1 = Employee("Susan Meyers",47899,"Accounting","Vice President")
employee2 = Employee("Mark Jones",39119,"IT","Programmer")
employee3 = Employee("Joy Rogers",81774,"Manufacturing","Engineer")

print(employee1.name,employee1.ID, employee1.Department,employee1.Title)
print(employee2.name,employee2.ID, employee2.Department,employee2.Title)
print(employee3.name,employee3.ID, employee3.Department,employee3.Title)
