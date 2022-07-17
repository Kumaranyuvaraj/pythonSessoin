class Pet:
    def __init__(self):
        self._cat ="The cat is jumping"
        

class Wild(Pet):

    def __init__(self):

        Pet.__init__(self)
        
        self._cat = "The cat is walking"
        print(self._cat )

obj1 = Pet()
obj2 = Wild()


    