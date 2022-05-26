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

def collect_regents_la_jolla():
    session = Session()
    html = session.get('https://www.regentslajolla.net/availableunits.aspx', headers={'User-Agent': 'Mozilla/5.0'}).content
    soup = BeautifulSoup(html, "html.parser")
    list = []
    for item in soup.find_all('tr', class_='AvailUnitRow'):
        name = 'Regents La Jolla'
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

def collect_regents_court():
    list = []
    list.append(_collect_regents_court_by_plan('https://www.liveatregentscourt.com/floorplans/san-miguel', 'San Miguel 1b1b'))
    list.append(_collect_regents_court_by_plan('https://www.liveatregentscourt.com/floorplans/santa-cruz', 'Santa Cruz 1b1b'))
    list.append(_collect_regents_court_by_plan('https://www.liveatregentscourt.com/floorplans/san-clemente', 'San Clemente 1b1b'))
    list.append(_collect_regents_court_by_plan('https://www.liveatregentscourt.com/floorplans/anacapa', 'Anacapa 1b1b'))
    list.append(_collect_regents_court_by_plan('https://www.liveatregentscourt.com/floorplans/main-top-island', 'Main Top Island 1b1b'))
    list.append(_collect_regents_court_by_plan('https://www.liveatregentscourt.com/floorplans/angel-island', 'Angel Island 1b1b'))
    list.append(_collect_regents_court_by_plan('https://www.liveatregentscourt.com/floorplans/point-reyes', 'Point Reyes 2b2b'))
    list.append(_collect_regents_court_by_plan('https://www.liveatregentscourt.com/floorplans/balboa-island', 'Balboa Island 2b2b'))
    list.append(_collect_regents_court_by_plan('https://www.liveatregentscourt.com/floorplans/santa-catalina', 'Santa Catalina 2b2b'))
    list.append(_collect_regents_court_by_plan('https://www.liveatregentscourt.com/floorplans/pahoa-island', 'Pahoa Island 2b2b'))
    list.append(_collect_regents_court_by_plan('https://www.liveatregentscourt.com/floorplans/santa-barbara', 'Santa Barbara 2b2b'))
    list.append(_collect_regents_court_by_plan('https://www.liveatregentscourt.com/floorplans/san-nicholas', 'San Nicholas 2b2b'))
    list.append(_collect_regents_court_by_plan('https://www.liveatregentscourt.com/floorplans/santa-rosa', 'Santa Rosa 3b3b'))
    unit_list = []
    for plan in list:
        for unit in plan:
            unit_list.append(unit)
    return unit_list

def _collect_regents_court_by_plan(url, floor_plan):
    session = Session()
    html = session.get(url, headers={'User-Agent': 'Mozilla/5.0'}).content
    soup = BeautifulSoup(html, "html.parser")
    list = []
    for item in soup.find_all('div', class_="fp-availApt-Container"):
        curr = Apartment()
        curr.name = 'Regents Court'
        curr.plan = floor_plan
        for info in item.find_all('span'):
            content = info.contents[0]
            if (content[0] == '#'):
                curr.apt = content
            else:
                curr.rent = content[12:]
        list.append(curr)
    return list