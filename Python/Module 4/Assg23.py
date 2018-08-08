'''
Created on 17-Jul-2018

@author: anitr
'''
class Faculty:
    def addExpertise(self,course):
        self.coursesExpertise.append(course)
    def __init__(self,name):
        self.__name = name
        self.__coursesExpertise=[]
class Student:
    def enroll(self,course):
        self.enrolledCourses.append(course)
    def __init__(self,student_id):
        self.__id = student_id
        self.__enrolledCourses=[]
class Course:
    def registerStudent(self,student):
        self.__registeredStudents.append(student)
    def registerExpert(self,faculty):
        self.expertFaculties.append(faculty)
    def __init__(self,name):
        self.__name=name
        self.__registeredStudents=[]
        self.__expertFaculties=[]
