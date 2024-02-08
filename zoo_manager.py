
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species 
        
    def __str__(self):
        return f'Name: {self.name}, Species: {self.species}'
    
    def speak(self):
        return ('Animal sound')

class Mammal(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)
        
    def give_birth(self):
        return (f'{self.name} the {self.species} has given birth')
    
class Primate(Mammal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def climb_trees(self):
        return f'{self.name} the {self.species} is climbing trees'
    
class Marsupial(Mammal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def carry_baby(self):
        return f'{self.name} the {self.species} is carrying its baby'
    
        
class Bird(Animal):
    def __init__(self, name, species, wingspan):
        super().__init__(name, species)
        self.wingspan = wingspan 

class Reptile(Animal):
    def __init__(self, name, species):
        super().__init__(name, species)

    def bask_in_sun(self):
        return f'{self.name} the {self.species} is basking in the sun'
    
class Aviary:
    def __init__(self, birds = []):
        self.birds = birds

    def add_birds(self, bird):
        self.birds.append(bird)
    
class ReptileEnclosure:
    def __init__(self, reptiles = []):
        self.reptiles = reptiles

    def add_reptiles(self, reptiles):
        self.reptiles.append(reptiles)



