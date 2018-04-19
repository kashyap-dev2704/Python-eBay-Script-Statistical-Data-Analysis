import ebaysdk
from ebaysdk.finding import Connection as finding
import statistics   #for doing average and median
import re #for using regular expression
import csv
import pandas as pd
from pandas import DataFrame
import os.path
import time



def check_if_already_exists (all_data):

    filepath = all_data[0]
    cardname = all_data[1]
    edition = all_data[2]
    number_of_searchResults = all_data[3]
    eBayHigh = all_data[4]
    eBayMedian = all_data[5]
    eBayLow = all_data[6]
    eBayAverage = all_data[7]
    eBayFoil = all_data[8]
    iD = all_data[9]
    

    #df = pd.read_csv('MAGIC_CARDS.csv',index_col='id')
    #b = (df.index[(df['englishName']  == '{}'.format(cardname)) & (df['edition'] == '{}'.format(edition))].tolist())

    dict_cards = {'iD':str(iD), 'Cardname':str(cardname),'Edition':str(edition),'No. of Search Results':str(number_of_searchResults),'eBay High':str(eBayHigh),'eBay Median':str(eBayMedian),'eBay Low':str(eBayLow),'eBay Average':str(eBayAverage),'eBay Foil':str(eBayFoil)}

    with open (filepath,'r') as file_read:

        headers = ['iD', 'Cardname', 'Edition', 'No. of Search Results', 'eBay High', 'eBay Median', 'eBay Low', 'eBay Average', 'eBay Foil']
        reader = csv.DictReader(file_read, delimiter=',', lineterminator='\n',fieldnames=headers)

        for row in reader:

            if row ==  dict_cards:
                return True

        return False


def writing_all_cards(all_data):

    filepath = all_data[0]
    cardname = all_data[1]
    edition = all_data[2]
    number_of_searchResults = all_data[3]
    eBayHigh = all_data[4]
    eBayMedian = all_data[5]
    eBayLow = all_data[6]
    eBayAverage = all_data[7]
    eBayFoil = all_data[8]
    iD = all_data[9]
   # t = time.localtime()
    #timestamp = time.strftime('%d-%b-%Y@%H:%M', t)
    

    #df = pd.read_csv('MAGIC_CARDS.csv',index_col='id')
    #b = (df.index[(df['englishName']  == '{}'.format(cardname)) & (df['edition'] == '{}'.format(edition))].tolist())
    #print(b[0])
    dict_csv = {'iD':iD, 'Cardname':cardname,'Edition':edition,'No. of Search Results':number_of_searchResults,'eBay High':eBayHigh,'eBay Median':eBayMedian,'eBay Low':eBayLow,'eBay Average':eBayAverage ,'eBay Foil':eBayFoil}
    #print(dict_csv)
    keys = dict_csv.keys()

    with open(filepath, "a") as csvfile:

        fileEmpty = os.stat(filepath).st_size == 0
        headers = ['iD', 'Cardname', 'Edition', 'No. of Search Results', 'eBay High', 'eBay Median', 'eBay Low', 'eBay Average', 'eBay Foil']
        writer = csv.DictWriter(csvfile, delimiter=',', lineterminator='\n',fieldnames=headers)

        if fileEmpty:
            writer.writeheader()

        writer.writerow(dict_csv)
        




def writing_in_file(filepath, condition_data, basic_data, analysed_data, foil, iD, cardName):
    #print(condition_data)
    condition_of_card =  list((object['condition'] for object in condition_data))
    #print('csvfile',condition_of_card)
    #Prefix = basic_data['prefix']
    Card_Name = cardName
    #print(Card_Name)
    iD = iD
    #print(iD)
    Edition = basic_data['Edition']

    Number_of_Search_Results = analysed_data['eBay Search Results']
    eBAY_High = analysed_data['eBay High']
    eBAY_Median = analysed_data['eBay Median']
    eBAY_Low = analysed_data['eBay Low']
    eBAY_Average = analysed_data['eBay Average']

    all_values = filepath, Card_Name, Edition, Number_of_Search_Results, eBAY_High, eBAY_Median, eBAY_Low, eBAY_Average, foil, iD
    
    for item in condition_of_card:

        if item == 'Not Defined':
             if check_if_already_exists (all_values) == False:
                writing_all_cards(all_values)

        elif item == 'Played':
            if check_if_already_exists (all_values) == False:
                writing_all_cards(all_values)

        elif item == 'Near Mint':
            if check_if_already_exists (all_values) == False:
                writing_all_cards(all_values)

        elif item == 'Good':
            if check_if_already_exists (all_values) == False:
                writing_all_cards(all_values)

        elif item == 'Excellent':
            if check_if_already_exists (all_values) == False:
                writing_all_cards(all_values)

        else:
            item = 'Damaged'
            if check_if_already_exists (all_values) == False:
                writing_all_cards(all_values)



def overall_writing_in_csv(data_foil, complete_data_of_normal, complete_data_of_foil):
    if data_foil == 'Normal':
        writing_in_file(complete_data_of_normal[0], complete_data_of_normal[1], complete_data_of_normal[2], complete_data_of_normal[3], 'Normal', complete_data_of_normal[4], complete_data_of_normal[5])
    else:
        data_foil == 'Foil'
        writing_in_file(complete_data_of_foil[0], complete_data_of_foil[1], complete_data_of_foil[2], complete_data_of_foil[3], 'Foil', complete_data_of_foil[4], complete_data_of_foil[5])


        
            
    
