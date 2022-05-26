class Apartment:
    def __init__(self):
        self.name = "Not Found"
        self.plan = "Not Found"
        self.apt = "Not Found"
        self.rent = "Not Found"
        self.av_date = "Not Found"
    
    def info(self):
        return ('\tName: ' + self.name + '\tPlan: ' + self.plan + '\tApt: ' + self.apt + 
        '\tRent: ' + self.rent + '\tMoveInDate: ' + self.av_date)

    def info_json(self):
        return ('{Name: ' + self.name + ', Plan: ' + self.plan + ', Apt: ' + self.apt + 
        ', Rent: ' + self.rent + ', MoveInDate: ' + self.av_date + '}')

    def table_header(self):
        return ['Name', 'Floor Plan', 'APT', 'Rent', 'Move in Date']

    def info_table(self):
        return [self.name, self.plan, self.apt, self.rent, self.av_date]