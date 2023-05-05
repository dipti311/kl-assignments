'''print("hello world")
str="hi"
print(type(str))
print(str[:-1])
a=["banan","red",3]
print("name:%s,id:%d"%(a[0],a[2]))
print(a[0:])'''
rockwell_employee=["shyam","ram"]
knowledgelens_employee=["mohan","chinmaya"]
salary_knowledgelens=[1000,2000,50000,7000]
employee_database=knowledgelens_employee+rockwell_employee
print(employee_database)
print("shyam" in employee_database)
for employee in employee_database:
    print(employee)
for employee in range(1):
   employee_database.append(input("enter the new employee"))
print(employee_database)

employee_database.remove("shyam")
print(employee_database)
print(max(salary_knowledgelens))

