# Credit to http://www.jesshamrick.com/2011/05/18/an-introduction-to-classes-and-inheritance-in-python/
# for exercises 

class Pet(object):
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def getName(self):
        return self.name

    def getSpecies(self):
        return self.species

    def __repr__(self):
        return "%r %r" % (self.name, self.species)

    def __str__(self):
        return "%s is a %s." % (self.name, self.species)

class Dog(Pet):
    def __init__(self, name, chases_cats):
        super(Dog, self).__init__(name, "Dog")
        self.chases_cats = chases_cats

    def chasesCats(self):
        return self.chases_cats

class Cat(Pet):
    def __init__(self, name, hates_dogs):
        super(Cat, self).__init__(name, "Cat")
        self.hates_dogs = hates_dogs

    def hatesDogs(self):
        return self.hates_dogs
