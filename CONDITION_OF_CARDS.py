import ebaysdk
from ebaysdk.finding import Connection as finding
import statistics   #for doing average and median
import re #for using regular expression
from collections import Counter

def check_condition(title_str):
            condition_regex= re.compile("(Near Mint)|(NM)|(Excellent)|(EXC)|(light played)|(lightly played)|(Good)|(GD)|(moderately played)|(MP)|(Played)|(heavily played)|(HP)|(damage)|(damaged)|"
            , re.IGNORECASE)
            condition_res = condition_regex.findall(title_str)
            condition = 'Not_Defined'
            for item in condition_res:
                #Near Mint
                temp = item[0]
                if temp:
                    condition = 'Near_Mint'
                temp = item[1]
                if temp:
                    condition = 'Near_Mint'
                    #Excellent
                temp = item[2]
                if temp:
                    condition = 'Excellent'
                temp = item[3]
                if temp:
                    condition = 'Excellent'
                temp = item[4]
                if temp:
                    condition = 'Excellent'
                temp = item[5]
                if temp:
                    condition = 'Excellent'
                    #Good
                temp = item[6]
                if temp:
                    condition = 'Good'
                temp = item[7]
                if temp:
                    condition = 'Good'
                temp = item[8]
                if temp:
                    condition = 'Good'
                temp = item[9]
                if temp:
                    condition = 'Good'
                    #played
                temp = item[10]
                if temp:
                    condition = 'Played'
                temp = item[11]
                if temp:
                    condition = 'Played'
                temp = item[12]
                if temp:
                    condition = 'Played'
                    #damaged
                temp = item[13]
                if temp:
                    condition = 'Damaged'
                temp = item[14]
                if temp:
                    condition = 'Damaged'
            return condition



def get_condition_offered_cards(data):

    title_offered = [x.get('title') for x in data[:]]
    #print (title_offered)

    data_based_on_condition = []
    #d_foil = []
    for item in title_offered:

        condition = check_condition (item)

        data_based_on_condition.append(condition)
        data_of_condition = Counter(data_based_on_condition)
        #print('1234',data_of_condition)


    return {'Condition of the Offered Cards':data_based_on_condition}



#def condition_count(condition_list):
    #data_of_condition = Counter(condition_list)
    #print(data_of_condition)
    
    
