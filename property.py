# class Student:
#     def __init__(self,name,grade):
#         self.name = name
#         self.grade = grade
        
#     @property
#     def msg(self):
#         return self.name +  " got grade " + self.grade
    
#     # def setter(self,msg):
#     #     send = msg.split(" ")
#     #     print(send)
#     #     self.name = send[0]
#     #     self.grade = send[-1]
    
#     @msg.setter
#     def msg(self,msg):
#         send = msg.split(" ")
#         print(send)
#         self.name = send[0]
#         self.grade = send[-1]

# stud = Student("Kumaran","A")
# # stud.setter("Kishore got grade B")
# stud.msg = "Kishore got grade B"
# print('name:',stud.name)
# print('grade:',stud.grade)
# print(stud.msg)


class Student:
    
    def __init__(self,name,grade):
        self.name = name
        self.grade = grade
         
    @property
    def msg(self):
        return self.name + " got grade " + self.grade
    
    @msg.setter
    def msg(self,msg):
        send = msg.split(" ")
        print(send)
        stud.name = send[0]
        stud.grade = send[-1]

stud = Student("Kumaran","A")

print(stud.name)
# stud.settr("Kishore got O grade")
stud.msg = "Kishore got O grade"
stud.grade = "B"
print(stud.grade)
print(stud.msg)




