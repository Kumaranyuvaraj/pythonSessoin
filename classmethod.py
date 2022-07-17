class Student:
    # counter = 0
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        # Student.counter = Student.counter+1
    
    def msg(self):
        # print(self.name  + " got the grade " + self.marks)
        return (self.name  + " got the grade " + self.marks)
    
    # @classmethod
    # def object_count(cls):
    #     return cls.counter
    
    @classmethod
    def get_per(cls,name,marks):
        return cls(name,str((int(marks)/600)*100))
        
s1 = Student("ria","20")
marks ='560'
name = 'nia'
# marks1 = str((int(marks)/600)*100)

s2 = Student.get_per(name, marks)
print(s2.msg())
# s2 = Student("dia","10")
# print(s1.msg())
# print(s2.msg())

# print(Student.object_count())
# print(s1.object_count())

