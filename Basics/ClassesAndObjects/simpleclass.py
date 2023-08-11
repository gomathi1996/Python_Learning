class Human:

    def name(self):
        print('Name')

    def age(self):
        print('Age')    

# human = Human()
# human.name()
# human.age()        

class Batsman(Human):
    def runs(self):
        print("Runs scored")
    
    
batsmn1 = Batsman()
batsmn1.age()