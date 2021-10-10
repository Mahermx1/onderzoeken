
import random

class Main():
    def __init__(self):
        self.People = []
        self.Stocks = []
        self.Wealth = 0

    def create_population(self, size):
        self.People = []
        for i in range(0, size):
            person = People()
            self.People.append(person)
            
    def create_stocks(self, size):
        self.Stocks = []
        for i in range(0, size):
            stock = Stocks()
            self.Stocks.append(stock)

    def RunIntoStock(self, runs):
        for i in range(0, runs):
            for person in self.People:
                stock = random.choice(self.Stocks)
                stock.encounter += 1
                # for u in range(0, stock.encounter):
                #     self.Stocks.append(stock)
                print('Man came across stock ')
                print('Stock risk is {0}'.format(stock.chance))
                print('Man had {0}'.format(person.money))
                person.Trade(stock.chance)
                print('And now {0}'.format(person.money))
                person.Broke()
                print('Is he broke {0}'.format(person.broke))
                print('---------------------------------')

            
            # filters out the broke
            self.People = list(filter(lambda person: person.broke == False, self.People))

    def addwealth(self):
        for person in self.People:
            self.Wealth += person.money

    def simulate(self):
        self.create_population(10)

        self.create_stocks(10)

        self.RunIntoStock(1)
        
        self.addwealth()

        self.results()

    def results(self):
        print('amount of moeny left : {0}'.format(round(self.Wealth)))
        print('amount of People left with more than 500: {0}'.format(len(self.People)))


class People():
    def __init__(self):
        self.chance = 0.5
        self.money = 1000
        self.broke = False

    def Broke(self):
        if (self.money <= 0):
            self.broke = True
    
    def Trade(self, risk):
        rng = random.random()
        if  (rng <= risk):
            self.money = self.money - (self.money * risk)
        else:
            self.money = self.money + (self.money * risk)

class Stocks():
    def __init__(self):
        self.chance = random.random()
        self.encounter = 0
    
    
if __name__ == "__main__":
    main = Main()
    main.simulate()
