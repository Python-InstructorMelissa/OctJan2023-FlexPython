class Player:
    # Constructor Function - container all attributes that will describe the instance in this case the player.  Inside the () are the attributes that are required to be declared on instance creation
    def __init__(self, name, teamColor):
        self.name = name
        self.health = 100
        self.inventory = []
        self.teamColor = teamColor

# functions below the constructor are all methods - these are things that the instance can do
    def printPlayer(self):
        print(f"{self.name}:\nTeam Color: {self.teamColor}\nCurrent Health: {self.health}")
        self.printInventory()
        print(f"\n\n\n")
        return self
    
    def printInventory(self):
        for i in self.inventory:
            print(f"{i.itemName}")
        return self
    
    def foundItem(self, item):
        self.inventory.append(item)
        # self.printInventory()
        return self
    
    def fight(self, other):
        for i in self.inventory:
            if i.itemType == "weapon":
                selfChoice = i.itemName
                selfPower = i.power
        for i in other.inventory:
            if i.itemType == "weapon":
                otherChoice = i.itemName
                otherPower = i.power
        print(f"{self.name} and {other.name} have gotten into a fight\n{self.name} is using {selfChoice} as a weapon and {other.name} is using {otherChoice}.")
        if selfPower > otherPower:
            other.health = other.health-selfPower
            print(f"Fight Results:\n\n{self.name}'s health is {self.health} and {other.name}'s is {other.health}\n\n{self.name} Won")
        if otherPower > selfPower:
            self.health = self.health-otherPower
            print(f"Fight Results:\n\n{self.name}'s health is {self.health} and {other.name}'s is {other.health}\n\n{other.name} Won")
        
        



class Item:
    def __init__(self, itemName, itemType, power):
        self.itemName = itemName
        self.itemType = itemType
        self.durability = 100
        self.power = power

    def printItem(self):
        print(f"{self.itemName}:\nItem Type: {self.itemType}\nCurrent Durability Remaining: {self.durability}\nPower item deals: {self.power}\n\n")
        return self
    

# Instance Creations

# To create an instance we use a variable (melissa and stephanie) set it = to the class name and then put it's attributes we are setting
melissa = Player("Melissa", "Blue")
stephanie = Player("Stephanie", "Maroon")


sword = Item("Slayer", "weapon", 10)
bowArrow = Item("Bow & Arrow", "weapon", 7)
healingPotion = Item("Healing Potion", "consumable", 10)




# Method usage

# WE use the methods by calling the instance variable then . and the function or method we want the instance to do.  As long as there is a return statement methods can be chained

# melissa.printPlayer()
# stephanie.printPlayer()
# sword.printItem()
# bowArrow.printItem()
# healingPotion.printItem()
melissa.foundItem(sword).foundItem(bowArrow).foundItem(bowArrow)
melissa.printPlayer()
stephanie.foundItem(bowArrow).foundItem(healingPotion).printPlayer().foundItem(sword)
melissa.fight(stephanie)
melissa.fight(stephanie)
melissa.fight(stephanie)