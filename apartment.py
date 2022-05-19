class Apartment:
    def __init__(self):
        self.name = "None"
        self.plan = "None"
        self.apt = "None"
        self.rent = "None"
        self.av_date = "None"
    
    def info(self):
        print ('{Name: ' + self.name + ', Plan: ' + self.plan + ', Apt: ' + self.apt + 
        ', Rent: ' + self.rent + ', Available: ' + self.av_date + '}')