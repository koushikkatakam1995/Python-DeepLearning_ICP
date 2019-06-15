class Employee:
    counter = 0
    salary_sum = 0

    def __init__(self, n, f, s, d):
        self.name = n
        self.family = f
        self.salary = s
        self.department = d
        Employee.counter += 1
        Employee.salary_sum += s

    def  get_avg_sal(self):
        average_sal = self.salary_sum / self.counter
        print("The average salary is: " +str(average_sal))
        return

    def display(self):
        print("Name:"+self.name, "Family:"+self.family, "Salary:" + str(self.salary), "Department:"+self.department)


class FulltimeEmployee(Employee):
    def __init__(self,n,f,s,d):
        Employee.__init__(self,n,f,s,d)
    e1 = Employee("Koushik", "Katakam", 45000, "CS")
    e2 = Employee("Kireeti", "Katakam", 95000, "CS")
    e3 = Employee("Venkateshwarlu", "Katakam", 100000, "CS")
    e1.display()
    e2.display()
    e3.display()


e4 = FulltimeEmployee("Vishala", "Katakam", 50000, "CS")
e4.display()
Employee.get_avg_sal(Employee)
