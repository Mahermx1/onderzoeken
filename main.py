import random

class Main():
    def __init__(self):
        self.People = []
        self.Stocks = []
        self.Avoid = False

    def create_population(self, size, nationality, chance):
        for i in range(0, size):
            person = People()
            person.chance = chance
            person.nationality = nationality
            self.People.append(person)
        
            
    def create_stocks(self, size):
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
                    print('nationality is {0}'.format(person.nationality))
                    print('chance is {0}'.format(person.chance))
                    print('Stock risk is {0}'.format(stock.risk))
                    self.AvoidIt(person.chance, stock.risk)
                    if (self.Avoid):
                        print('Didnt avoid')
                        stock.encounter += 1
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

    def addwealth(self, nationality):
        self.Wealth = 0
        for person in self.People:
            if (person.nationality == nationality):
                self.Wealth += person.money
        return self.Wealth

    def simulate(self):
        self.create_population(100, "ecuador", 0.67)
        self.create_population(100, "singapore", 0.08)
        self.create_population(100, "portugal", 0.99)

        random.shuffle(self.People)

        self.create_stocks(100)

        self.RunIntoStock(1)

        self.results()

    def results(self):
        print('amount of money left ecuador : {0}'.format(round(self.addwealth("ecuador"))))
        print('amount of money left portugal : {0}'.format(round(self.addwealth("portugal"))))
        print('amount of money left singapore: {0}'.format(round(self.addwealth("singapore"))))
        print('amount of People who are not broke: {0}'.format(len(self.People)))


class People():
    def __init__(self):
        self.chance = random.uniform(0.3,0.6)
        self.money = 1000
        self.broke = False
        self.encounterchance = random.random()
        self.nationality = "nothing"

    def Broke(self):
        if (self.money <= 0):
            self.broke = True

    def Trade(self, risk):
        rng = random.random()
        if  (rng < risk):
            self.money = self.money - ((self.money*1.5) * risk)
        else:
            self.money = self.money + ((self.money*1.5) * risk)

class Stocks():
    def __init__(self):
        self.risk = random.random()
        self.encounter = 0

    
    
if __name__ == "__main__":
    main = Main()
    main.simulate()
