'''
Created on 17-Jul-2018

@author: anitr
'''
class Employee: 
    @classmethod
    def from_string(cls,emp_str):
        cls.emp_str=emp_str.split('-')
        cls.first=cls.emp_str[0]
        cls.last=cls.emp_str[1]
        cls.pay=cls.emp_str[2]
        print('',cls.first,'\n',cls.last,'\n',cls.pay)
    def __init__(self,first,last,pay):
        self.firstname = first
        self.lastname = last
        self.pay = pay
emp_1_str = 'John-Abraham-50000'
emp_1 = Employee.from_string(emp_1_str)