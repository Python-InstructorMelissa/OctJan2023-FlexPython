# Instance - 1 example of what we wanted to make
# Method - Function that belongs to the thing we make - action it can perform
# Attributes - Describe the things we want to make (descriptive)
# Constructor - The part that makes what we want to make
# class - Blueprint for what we want to make (will be an object or dictionary)

# class:
    # constructor:
        # attributes
    # methods:

# instances

# a class is the name of what we will make, the constructor contains the attributes that each item we make must have and methods are what the item can do these are all contained inside the class.  Instances are what we have made


class AnimalType:
    def __init__(self, appendages, climate, foodType, species, id):
        self.appendages = appendages
        self.climate = climate
        self.foodType = foodType
        self.species = species
        self.id = id


class Animal(AnimalType):
    def __init__(self, data, name, age):
        super(data)
        self.name = name
        self.age = age
    
    def eating(self, food):
        if self.foodType == "Carnivore":
            print(f"{self.name} hunted down a {food} and ate like a royal")
            return self
        if self.foodType == "Omnivore":
            print(f"{self.name} was given {food} to eat")
            return self
        if self.foodType == "Herbivore":
            print(f"{self.name} walked through the garden and found {food} and ate comfortably")
            return self


class Product:
    pass




# Creating Instances
pig = AnimalType(4, "Temperate", "Omnivore", "pig", 1)

wilber = Animal(pig, "Wilber", 1)
bob = Animal(pig, "Bob", 3)


# Running Methods
bob.eating("slop")