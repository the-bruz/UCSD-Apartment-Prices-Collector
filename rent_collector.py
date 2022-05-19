import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from apartment import Apartment

def collect_garden_comm(name, url):
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
            curr.info()
    
    for a in list: a.info()
    return list

def collect_cvv():
    return collect_garden_comm('Costa Verde Village', 'https://www.on-site.com/web/online_app/choose_unit?goal=6&attr=x20&property_id=1166&lease_id=0&unit_id=0&required=')

def collect_towers():
    return collect_garden_comm('Towers At Costa Verde','https://www.on-site.com/web/online_app/choose_unit?goal=6&attr=x20&property_id=1167&lease_id=0&unit_id=0&required=')

def collect_360_lux():
    return collect_garden_comm('360 Luxury','https://www.on-site.com/web/online_app/choose_unit?goal=6&attr=x20&property_id=191247&lease_id=0&unit_id=0&required=')

def collect_lux():
    return collect_garden_comm('Lux UTC', 'https://www.on-site.com/web/online_app/choose_unit?goal=6&attr=x20&property_id=225322&lease_id=0&unit_id=0&required=')

def collect_crossroads():
    return collect_garden_comm('La Jolla Crossroads', 'https://www.on-site.com/web/online_app/choose_unit?goal=6&attr=x20&property_id=21385&lease_id=0&unit_id=0&required=')

def collect_la_regencia():
    return collect_garden_comm('La Regencia', 'https://www.on-site.com/web/online_app/choose_unit?goal=6&attr=x20&property_id=1360&lease_id=0&unit_id=0&required=')