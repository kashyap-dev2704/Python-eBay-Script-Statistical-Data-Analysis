import ebaysdk
from ebaysdk.finding import Connection as finding
import statistics   #for doing average and median
import re #for using regular expression

def amount_of_cards(test_str):  #function for amount of cards
    quantity_regex = re.compile("(\d)x|x(\d)|(playset)|(\d\d)x",re.IGNORECASE)
    res = quantity_regex.findall(test_str)
    print(res)
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
        temp = item[3] * 1
        if temp:
            quantity = temp
    return quantity
    

amount_of_cards("2 adidas Shoes")

 

#(\d\d)x |(\d)x |x(\d) |x(\d\d) | (playset)
