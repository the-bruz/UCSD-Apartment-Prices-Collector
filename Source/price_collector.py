from requests import Session
from urllib.request import urlopen
from bs4 import BeautifulSoup
from apartment import Apartment

def _collect_garden_comm(name, url):
    html = urlopen(url).read()
    soup = BeautifulSoup(html, "html.parser")
    list = []
    for item in soup.find_all('div', class_='floor_plan'):
        plan_name = item.find_all('p', class_='floor_plan_name')[0].contents[0]
        if (plan_name == 'Lease Add-On'): continue

        apts = item.find_all('td', class_='addr_or_apt')
        rents = item.find_all('span', class_='rent_amount')
        av_dates = item.find_all('div', class_='show_available_date')

        for i in range(len(apts)):
            curr = Apartment()
            curr.name = name
            curr.plan = plan_name.strip()
            curr.apt = apts[i].contents[0].strip()
            curr.rent = rents[i].contents[0].strip()
            curr.av_date = av_dates[i].contents[0].strip()
            list.append(curr)
    return list

def collect_cvv():
    return _collect_garden_comm('Costa Verde Village', 'https://www.on-site.com/web/online_app/choose_unit?goal=6&attr=x20&property_id=1166&lease_id=0&unit_id=0&required=')

def collect_towers():
    return _collect_garden_comm('Towers at Costa Verde','https://www.on-site.com/web/online_app/choose_unit?goal=6&attr=x20&property_id=1167&lease_id=0&unit_id=0&required=')

def collect_360_lux():
    return _collect_garden_comm('360 Luxury','https://www.on-site.com/web/online_app/choose_unit?goal=6&attr=x20&property_id=191247&lease_id=0&unit_id=0&required=')

def collect_lux():
    return _collect_garden_comm('Lux UTC', 'https://www.on-site.com/web/online_app/choose_unit?goal=6&attr=x20&property_id=225322&lease_id=0&unit_id=0&required=')

def collect_crossroads():
    return _collect_garden_comm('La Jolla Crossroads', 'https://www.on-site.com/web/online_app/choose_unit?goal=6&attr=x20&property_id=21385&lease_id=0&unit_id=0&required=')

def collect_la_regencia():
    return _collect_garden_comm('La Regencia', 'https://www.on-site.com/web/online_app/choose_unit?goal=6&attr=x20&property_id=1360&lease_id=0&unit_id=0&required=')

def collect_regents_lajolla():
    session = Session()
    html = session.get('https://www.regentslajolla.net/availableunits.aspx', headers={'User-Agent': 'Mozilla/5.0'}).content
    soup = BeautifulSoup(html, "html.parser")
    list = []
    for item in soup.find_all('tr', class_='AvailUnitRow'):
        name = 'Regents LaJolla'
        sqft = item.find('td', attrs={'data-label': 'Sq. Ft.'}).contents[0]
        if (sqft == '753'): plan_name = 'Ruby 1b1b'
        if (sqft == '1102'): plan_name = 'Pearl 2b2b'
        if (sqft == '1110'): plan_name = 'Garnet 2b2b'
        if (sqft == '1117'): plan_name = 'Jewel/Emerald 2b2b'
        if (sqft == '1210'): plan_name = 'Opal 2b2b'
        apt = item.find('td', attrs={'data-label': 'Apartment'}).contents[0]
        rent = item.find('td', attrs={'data-label': 'Rent'}).contents[0]
        
        action = item.find('input', attrs={'type': 'button'})
        action = action['onclick']
        av_date = action[action.find('MoveInDate') + 11:action.find('\')')]
        curr = Apartment()
        curr.name = name
        curr.plan = plan_name
        curr.apt = apt
        curr.rent = rent
        curr.av_date = av_date
        list.append(curr)
    return list