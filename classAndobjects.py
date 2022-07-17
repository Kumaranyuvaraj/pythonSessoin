# #Example 1: Creating Class and Object in Python

# class Bird:
#     #class attribute
#     species = 'Parrot'

#     #instance attribute

#     def __init__(self,name,color):
#         self.name = name
#         self.color = color
#         print("The Bird {} is {} color".format(self.name,self.color))

# b = Bird("Peacock","Blue")


# print("The Bird {} is green color".format(b.__class__.species))



#Example 2 : Creating Methods in Python

class Dog:

    def __init__(self,name,color):
        self.name = name
        self.color = color

    def display(self):
        print("The Dog {} is {} color".format(self.name,self.color))

d = Dog("Siberian","White")
d.display()


