class Batsman:

# this is the default function and should be created in all the class when parameters needs to be passed and it should have self as parameters and it can have other parameters as per requirements.

    def __init__(self,name,age,ipl_team):
        self.name = name
        self.age = age
        self.ipl_team = ipl_team

    def print_data(self):
        print("Name : "+self.name)
        print("Age : "+str(self.age))
        print("IPL Team : "+self.ipl_team)        