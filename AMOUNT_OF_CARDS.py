import ebaysdk
from ebaysdk.finding import Connection as finding
import statistics   #for doing average and median
import re #for using regular expression

def amount_of_cards(test_str):  #function for amount of cards
    quantity_regex = re.compile("(\d)x | x(\d) | (playset)",re.IGNORECASE)
    res = quantity_regex.findall(test_str)
    quantity = 1
    for item in res:
        temp = item[0] * 1
        if temp:
            quantity = temp
        temp = item[1] * 1
        if temp:
            quantity = temp
        temp = item[2]
        if temp!="":
            quantity = 4
    return quantity
