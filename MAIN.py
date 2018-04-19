import ebaysdk
from ebaysdk.finding import Connection as finding
import statistics   #for doing average and median
import re #for using regular expression
from AMOUNT_OF_CARDS import *
from ANALYSIS_OF_DATA import *
from CONDITION_OF_CARDS import *
from CSV_FILE import *
from CHECK_FOIL import *
from PROPER_KEY_GENERATION import *
import pandas as pd
from pandas import DataFrame

def getData(Prefix, CardName, Set, Language):
    key = '{} {} {} {}'.format(Prefix,CardName,Set,Language)
    #print(key)
    api = finding(siteid='EBAY-US', appid='PeerRich-Snapcard-PRD-38ad16031-09f66a66', config_file=None)
    
    api.execute('findItemsByKeywords', {
        'keywords': key,
        'itemFilter': [
            {'name': 'Format', 'value': 'All Listings'},
            #{'name': 'Condition', 'value': 'Used'},
            {'name': 'MinPrice', 'value': '0', 'paramName': 'Currency', 'paramValue': 'USD'},
            {'name': 'MaxPrice', 'value': '100000', 'paramName': 'Currency', 'paramValue': 'USD'}
        ],
        'paginationInput': {
            'entriesPerPage': '25',
            'pageNumber': '1'
        },
        'sortOrder': 'CurrentPriceHighest'
    })

    dictstr = api.response.dict()    #dictionary that shows all the values available for any product
    search_result_count = (dictstr['searchResult'])
    if search_result_count['_count'] == '0':
        return 
        
    information_of_cards = []            #list to store the data.
    for item in (dictstr['searchResult']['item']):
        data = {}
        data['itemID'] = item['itemId']
        data['title'] = item['title']
        data['categoryId'] = item['primaryCategory']['categoryId']
        data['offered_price'] = float(item['sellingStatus']['currentPrice']['value'])
        data['data_amt_cards'] =  float( amount_of_cards(item['title']))  # from AMOUNT_OF_CARDS page
        data['avg_offered_card_price'] = data['offered_price'] / data['data_amt_cards']
        data['condition'] = check_condition(item['title']) # from CONDITION_OF_CARDS page
        data['foil'] = check_foil(item['title']) # from CHECK_FOIL pae

        information_of_cards.append(data)

    return information_of_cards
    
def main():

    allKeys = getListOfPerfectKey('K:\Snapp.ai\Final_PROJECT\DATA\Karstern\Demo.csv')
    #print(allKeys)
    Language = ''   #for language first letter should always be capital and other letters should be small.
    for item in allKeys:
        
        try:
            prefix = item['prefix']
            CardName = item['cardname']
            Edition = item['edition']
            cardKey = item['cardname_for_key']
            #print("CARDKEY",cardKey)
            iD = item['iD']
            
            basic_detail_of_card = {'prefix' : prefix, 'CardName' : CardName, 'Edition' : Edition}
            data_description = getData(prefix, cardKey, Edition, Language)
            if(data_description == None):
                print("NO RESULTS FOUND {} {} {}".format(iD, CardName, Edition))
                continue    #continue statement rejects all the down statement and goes to the top of the function.
       
            data_condition = get_condition_offered_cards(data_description)  # from CONDITION_OF_CARDS page
            data_foil = list_of_foil(data_description)
                
                       
            for item in data_foil:
                if item == 'Normal':
                    data_analysis = check_normal_of_cards(data_description)
                    complete_data_of_normal = ('k:/Snapp.ai/Final_PROJECT/DATA/SOLD_CARDS/English/mtg.csv', data_description, basic_detail_of_card, data_analysis, iD, CardName)
                    overall_writing_in_csv(item, complete_data_of_normal, None)
                else:
                    data_analysis_foil = check_foil_of_cards(data_description)
                    complete_data_of_foil = ('k:/Snapp.ai/Final_PROJECT/DATA/SOLD_CARDS/English/mtg.csv', data_description, basic_detail_of_card, data_analysis_foil, iD, CardName)
                    overall_writing_in_csv(item, None, complete_data_of_foil)
        except:
            print("This Magic Card Does Not Work {} {} {}".format(iD,CardName, Edition))
            pass

if __name__ == '__main__':
    main()
