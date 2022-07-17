class Dog:
    def __init__(self):
        print("The dog is ready")

    def run(self):
        print("The dog is running")

class Pet(Dog):
    

    def __init__(self):
        super().__init__()
        print("The dog is barking")

    def swim(self):
        print("The dog is ready to swim")

p =Pet()
p.run()
p.swim()
