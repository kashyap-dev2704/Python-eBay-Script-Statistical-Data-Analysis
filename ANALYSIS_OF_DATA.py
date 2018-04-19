import ebaysdk
from ebaysdk.finding import Connection as finding
import statistics   #for doing average and median
import re #for using regular expression
import pandas as pd
from pandas import DataFrame


def check_foil_of_cards(data):
    price_of_articles = [x.get('avg_offered_card_price') for x in data[:]]
    #print ('FOIL PRICE OF ALL CARDS', price_of_articles)
    foil_condition = [x.get('foil') for x in data[:]]
    #print ('FOIL OR NORMAL', foil_condition)
    foil_keys = {'Price of Foil Cards':price_of_articles, 'Foil':foil_condition}
    #print ('DICTONARY OF FOIL CARDS',foil_keys)

    df = pd.DataFrame (foil_keys)
    price_foil_cards = df[df.Foil == 'Foil']
    list_of_foilcard_prices = price_foil_cards['Price of Foil Cards'].tolist()
    #print('PRICES OF FOIL',list_of_foilcard_prices)

    eBayHigh = round(max(list_of_foilcard_prices),2)
    eBayLow = round(min(list_of_foilcard_prices),2)
    eBayMedian = round(statistics.median(list_of_foilcard_prices),2)
    eBayAverage = round(statistics.mean(list_of_foilcard_prices),2)
    eBayNoOfSearchResults = len(list_of_foilcard_prices) #it will only give length of no. of foil cards searched as a results.
    data_foil_analysis = {'eBay High':eBayHigh, 'eBay Median': eBayMedian, 'eBay Low':eBayLow, 'eBay Average':eBayAverage, 'eBay Search Results':eBayNoOfSearchResults}

    return data_foil_analysis


def check_normal_of_cards(data):
    price_of_articles = [x.get('avg_offered_card_price') for x in data[:]]
    #print ('FOIL PRICE OF ALL CARDS', price_of_articles)
    foil_condition = [x.get('foil') for x in data[:]]
    #print ('FOIL OR NORMAL', foil_condition)
    foil_keys = {'Price of Normal Cards':price_of_articles, 'Foil':foil_condition}
    #print ('DICTONARY OF FOIL CARDS',foil_keys)

    df = pd.DataFrame (foil_keys)
    price_normal_cards = df[df.Foil == 'Normal']
    list_of_normal_prices = price_normal_cards['Price of Normal Cards'].tolist()
    #print('PRICES OF NORMAL',list_of_normal_prices)

    eBayHigh = round(max(list_of_normal_prices),2)
    eBayLow = round(min(list_of_normal_prices),2)
    eBayMedian = round(statistics.median(list_of_normal_prices),2)
    eBayAverage = round(statistics.mean(list_of_normal_prices),2)
    eBayNoOfSearchResults = len(list_of_normal_prices) #it will only give length of no. of foil cards searched as a results.

    #data_normal_analysis = {'eBay Normal High':eBayHigh, 'eBay Normal Median': eBayMedian, 'eBay Low':eBayLow, 'eBay Average':eBayAverage}
    data_normal_analysis = {'eBay High':eBayHigh, 'eBay Median': eBayMedian, 'eBay Low':eBayLow, 'eBay Average':eBayAverage, 'eBay Search Results':eBayNoOfSearchResults}

    return data_normal_analysis
