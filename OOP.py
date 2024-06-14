#a class is a blueprint from which different objects are created
#when a new one is made, the variables are set here and can be accessed in the object

#constructors is when an object sets default values for the new project
#in python, the __init__ func adds value to object attributes
class character:
    def __init__(self, name, strength, health, defense):
        self.name=name
        self.strenght= strength
        self.health= health
        self.defense= defense
        #dot notation is using a dot or period to reference the attributes of an objeect
#^ this is the constructor for the class

#not you have to declare a class object

#object_name= character(name,strength,health,defense)
player1= character("Sage",10,100,2)
print(player1.name)
print(player1.strenght)
print(player1.health)
print(player1.defense)