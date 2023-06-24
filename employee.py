#write a python class employee with attributes like emp_id emp_name emp_salary and emp_department and methods like calculate emp_salary emp_assign_department and print_employee_details.
class Employee:
    emp_id=str(input("emp_id:"))
    emp_name=str(input("emp_name:"))
    emp_salary=float(input("emp_salary:"))
    emp_department=str(input("department:"))
    workedhrs=int(input("no of hours worked:"))
obj1=Employee
print("emp_id:",obj1.emp_id)
print("emp_name:",obj1.emp_name)
print("emp_department:",obj1.emp_department)
if obj1.workedhrs>50:
    overtime=workedhrs-50
    overtimeamt=(overtime*(salary/50))
    print("salary:",overtimeamt+obj1.emp_salary)
else:
    print("Salary:",obj1.emp_salary)