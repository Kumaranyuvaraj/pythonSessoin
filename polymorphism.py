class Organizations1:

    def reading(self):
        print("The student is reading")

class Organizations3:
    
    def playing(self):
        print("The Student is Playing")

class Organizations:

    def school(self,student):
        student.reading()
        

o1 = Organizations1()
o2 = Organizations3()
o = Organizations()

o.school(o1)


