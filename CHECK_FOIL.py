import ebaysdk
from ebaysdk.finding import Connection as finding
import re #for using regular expression



def check_foil(title_foil_str):
    foil_regex = re.compile("(foil)",re.IGNORECASE)
    foil_res = foil_regex.findall(title_foil_str)

    foil_cards = {}
    notfoil_cards = {}
    
    shine = 'Normal'
    for item in foil_res:
        temp = item[0]
        if temp:
            shine = 'Foil'
    return shine



def list_of_foil(data):
    foil_condition = [x.get('foil') for x in data[:]]
    return foil_condition











    
