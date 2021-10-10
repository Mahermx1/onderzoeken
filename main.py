
import random

class Main():
    def __init__(self):
        self.People = []
        self.Stocks = []
        self.Wealth = 0
        self.Avoid = False

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

    def AvoidIt(self, chance, risk):
        if  (chance <= risk):
            self.Avoid = False
        else:
            self.Avoid = True

    def RunIntoStock(self, rounds):
        for i in range(0, rounds):  
            for person in self.People:
                if (person.encounterchance <= 0.7):
                    print('encountered a stock ')
                    person.encounterchance = random.random()
                    stock = random.choice(self.Stocks)
                    print('Man came across stock ')
                    print('Stock risk is {0}'.format(stock.risk))
                    self.AvoidIt(person.chance, stock.risk)
                    if (self.Avoid):
                        print('Didnt avoid')
                        stock.encounter += 1
                        # for u in range(0, stock.encounter):
                        #     self.Stocks.append(stock)
                        print('Man had {0}'.format(person.money))
                        person.Trade(stock.risk)
                        print('And now {0}'.format(person.money))
                        person.Broke()
                        print('Is he broke {0}'.format(person.broke))
                    else:
                        print('avoided')

                else:
                    print('Didnt encounter')
                print('---------------------------------')

            
            # filters out the broke
            self.People = list(filter(lambda person: person.broke == False, self.People))

    def addwealth(self):
        for person in self.People:
            self.Wealth += person.money

    def simulate(self):
        self.create_population(1000)

        self.create_stocks(100)

        self.RunIntoStock(1)
        
        self.addwealth()

        self.results()

    def results(self):
        print('amount of moeny left : {0}'.format(round(self.Wealth)))
        print('amount of People who are not broke: {0}'.format(len(self.People)))


class People():
    def __init__(self):
        self.chance = random.uniform(0.3,0.6)
        self.money = 1000
        self.broke = False
        self.encounterchance = random.random()

    def Broke(self):
        if (self.money <= 0):
            self.broke = True

    def Trade(self, risk):
        rng = random.random()
        print (rng)
        print (self.money)
        if  (rng < risk):
            self.money = self.money - (1000 * risk)
        else:
            self.money = self.money + (1000 * risk)

class Stocks():
    def __init__(self):
        self.risk = random.random()
        self.encounter = 0

    
    
if __name__ == "__main__":
    main = Main()
    main.simulate()
