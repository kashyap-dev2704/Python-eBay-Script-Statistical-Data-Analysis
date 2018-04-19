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
    df = pd.read_csv('K:\Snapp.ai\Final_PROJECT\DATA\demo.csv')
    keywords = ['mtg','magic card','magic', 'mtg card']
    key = []
    for index, row in df.iterrows():
        for item in keywords:
            prefix = item
            CardName = row['CardName']
            Edition = row['Edition']
            Language = ''    #for language first letter should always be capital and other letters should be small.

            search = '{} {} {} {}'.format(prefix, CardName, Edition, Language)

            key.append(search)

            basic_detail_of_card = {'prefix' : prefix, 'CardName' : CardName, 'Edition' : Edition}

            data_description = getData(prefix, CardName, Edition, Language) # from MAIN(same) page
            if (data_description == None):
                continue  #continue statement rejects all the down statement and goes to the top of the function.
                
            data_condition = get_condition_offered_cards(data_description) # from CONDITION_OF_CARDS page
            #condition_classified_data = condition_count(data_condition)
            data_foil = list_of_foil(data_description)
            
            

            
            for item in data_foil:
                if item == 'Normal':
                    data_analysis = check_normal_of_cards(data_description)
                    complete_data_of_normal = ('k:/Snapp.ai/Final_PROJECT/DATA/SOLD_CARDS/English'+'/'+prefix+'.csv', data_description, basic_detail_of_card, data_analysis)
                    overall_writing_in_csv(item, complete_data_of_normal, None)
                else:
                    data_analysis_foil = check_foil_of_cards(data_description)
                    complete_data_of_foil = ('k:/Snapp.ai/Final_PROJECT/DATA/SOLD_CARDS/English'+'/'+prefix+'.csv', data_description, basic_detail_of_card, data_analysis_foil)
                    overall_writing_in_csv(item, None, complete_data_of_foil)

if __name__ == '__main__':
    main()
