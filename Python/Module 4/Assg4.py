'''
Created on 17-Jul-2018

@author: anitr
'''
class Employee:
    def __init__(self,first,last,pay):
        self.firstname = first
        self.lastname = last
        self.pay = pay
        self.email =first+'.'+last+'@company.com'
    def getmail(self):
        mail=self.email
        return mail
    def getfullname(self):
        full=self.firstname+' '+self.lastname
        return full
    def getpay(self):
        pay=self.pay
        return pay
emp_1 = Employee('Mohandas','Gandhi',50000)
print(emp_1.getfullname())
print(emp_1.getpay())
print(emp_1.getmail())