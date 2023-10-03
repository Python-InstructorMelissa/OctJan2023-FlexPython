class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.wallet = 0

    def printUser(self):
        print(f'{self.name} is {self.age} years old')
        return self
    
    def talk(self, other):
        print(f'{self.name} is going to call {other.name} about class')
        return self
    
    def birthday(self):
        self.age = self.age+1
        print(f"{self.name}'s birthday is today and they are now {self.age} years old")
        return self
    
    def purchaseGift(self, gift, other):
        amount = gift.cost
        if self.wallet < amount:
            print(f"{self.name} tried to purchase a {gift.name} but doesn't have enough money in their wallet")
        else:
            self.wallet = self.wallet - amount
            print(f'{self.name} was feeling good today and purchased {other.name} a {gift.name} as a gift')
        return self
    
    def printWallet(self):
        print(f'{self.name} has {self.wallet} in their wallet')
        return self

    def addCash(self, num):
        amount = int(num)
        self.wallet += int(amount)
        print(f"{self.name} added {num} to their wallet")
        return self


class Gift:
    def __init__(self, name, cost):
        self.name = name
        self.cost = cost

    def printGift(self):
        print(f'{self.name} cost ${self.cost}')
        return self




# Instances
robert = User("Robert", 35)
melissa = User("Melissa", 44)
nick = User("Nick", 41)

bee = Gift("Bee Plushy", 9.99)


# Method Usage
robert.printUser()
melissa.printUser()
robert.talk(melissa)
robert.printUser().birthday()
nick.addCash(8)
nick.addCash(5).printWallet()
bee.printGift()
nick.purchaseGift(bee, melissa)

