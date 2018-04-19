import csv
import statistics
import os
import time
import pymysql



def exsisting_data(filepath):
    data = []
    with open(filepath, 'r') as collectdata:
        collectdata.readline()
        csv_reader = csv.reader(collectdata, delimiter = ',')
        for col in csv_reader:
            data.append(col[2:3])
    id_list = [item for sublist in data for item in sublist]
    return list(set(id_list))

def averageOfData(totalData):
    result = [item for sublist in totalData for item in sublist]
    finalResult = [float(item) for item in result]
    averageFinalResult = statistics.mean(finalResult)
    return averageFinalResult

def extractingData(Id, filepath):
    all_data = []
    with open(filepath, 'r') as target:
        csv_reader = csv.reader(target)
        for col in csv_reader:
            condition = col[0] == Id
            #print(col[0][0])
            if condition == True:
                total_data = col[0:9]
                data_dict = {}
                data_dict['id'] = col[0:1]
                data_dict['CardName'] = col[1:2]
                data_dict['Edition'] = col[2:3]
                data_dict['noOfSearchResult'] = col[3:4]
                data_dict['eBayHigh'] = col[4:5]
                data_dict['eBayMedian'] = col[5:6]
                data_dict['eBayLow'] = col[6:7]
                data_dict['eBayAverage'] = col[7:8]
                all_data.append(data_dict)


    iD = [data_dict['id'] for data_dict in all_data]
    id_list = [item for sublist in iD for item in sublist]
    #id_act = (", ".join(id_list[0:1]))
    ID = id_list[0] # id_act[1:-1]

    cardname = [data_dict['CardName'] for data_dict in all_data]
    cardname_list = [item for sublist in cardname for item in sublist]
    cardname_act = (", ".join(cardname_list[0:1]))
    

    edition = [data_dict['Edition'] for data_dict in all_data]
    edition_list = [item for sublist in edition for item in sublist]
    edition_act = (", ".join(edition_list[0:1]))


    totalSearchResults = [data_dict['noOfSearchResult'] for data_dict in all_data]
    if len(totalSearchResults) == 0:
        return
    averageTotalSearchResults = averageOfData(totalSearchResults)

    totaleBayHigh = [data_dict['eBayHigh'] for data_dict in all_data]
    averageTotaleBayHigh = averageOfData(totaleBayHigh)

    totaleBayMedian = [data_dict['eBayMedian'] for data_dict in all_data]
    averageTotaleBayMedian = averageOfData(totaleBayMedian)

    totaleBayLow = [data_dict['eBayLow'] for data_dict in all_data]
    averageTotaleBayLow = averageOfData(totaleBayLow)

    totaleBayAverage = [data_dict['eBayAverage'] for data_dict in all_data]
    averageTotaleBayAverage = averageOfData(totaleBayAverage)

    t = time.localtime()
    timestamp = time.strftime('%d-%b-%Y@%H:%M', t)

    average_dict = {'Id' : ID, 'NameOfCard' : cardname_act, 'Edition' : edition_act,  'NoOfSearchResults' : averageTotalSearchResults, 'eBayHigh' : averageTotaleBayHigh, 'eBayMedian' : averageTotaleBayMedian, 'eBayLow' : averageTotaleBayLow, 'eBayAverage' : averageTotaleBayAverage }
    return average_dict

def checkingAverage(path, all_data):
    filepath = path
    
    ID = all_data['Id']
    cardname = all_data['NameOfCard']
    edition = all_data['Edition']
    number_of_searchResults = all_data['NoOfSearchResults']
    eBayHigh = all_data['eBayHigh']
    eBayMedian = all_data['eBayMedian']
    eBayLow = all_data['eBayLow']
    eBayAverage = all_data['eBayAverage']


    dict_avg = {'Id':ID, 'NameOfCard':str(cardname), 'Edition':str(edition), 'NoOfSearchResults':str(number_of_searchResults), 'eBayHigh':str(eBayHigh), 'eBayMedian':str(eBayMedian),'eBayLow':str(eBayLow),'eBayAverage':str(eBayAverage)}
    #print('AVERAGE',dict_avg)

    with open(filepath, "r") as averagefile:
        headers = ['Id', 'NameOfCard', 'Edition', 'NoOfSearchResults', 'eBayHigh', 'eBayMedian', 'eBayLow', 'eBayAverage', 'TimeStamp']
        reader = csv.DictReader(averagefile, delimiter=',', lineterminator='\n', fieldnames = headers)
        for row in reader:
            if row == dict_avg:
                return True
        return False
        writer.writerow(dict_csv)


def writingAverage(path, all_data):
    with open(path, "a") as avgfile:
        fileEmpty = os.stat(path).st_size==0
        t = time.localtime()
        timestamp = time.strftime('%d-%b-%Y@%H:%M', t)
        headers = ['Id', 'NameOfCard', 'Edition', 'NoOfSearchResults', 'eBayHigh', 'eBayMedian', 'eBayLow', 'eBayAverage', 'TimeStamp']
        writer = csv.DictWriter(avgfile, delimiter=',', lineterminator='\n', fieldnames = headers)
        
        all_data['TimeStamp'] = timestamp
        if fileEmpty:
            writer.writeheader()
        writer.writerow(all_data)


def writingSQL(all_data):
    #print("COMING")
    if all_data == None:
        return
    ID = all_data['Id']
    cardname = all_data['NameOfCard']
    edition = all_data['Edition']
    number_of_searchResults = all_data['NoOfSearchResults']
    eBayHigh = all_data['eBayHigh']
    eBayMedian = all_data['eBayMedian']
    eBayLow = all_data['eBayLow']
    eBayAverage = all_data['eBayAverage']
    
    t = int(round(time.time() * 1000))
    timestamp = t
    #timestamp = str(time.strftime('%d-%b-%Y@%H:%M', t))
    try:
        conn = pymysql.connect(host = 'snapcardster.com', port = 3306, user = 'ebay', passwd = 'ebay', db = 'ebay')    
        cur = conn.cursor()
        print("DB CONNECTION ESTABLISHED")
        sql = ("INSERT INTO `ebay`.`KASHYAP_TABLE` (`Id`, `NameOfCard`, `Edition`, `NoOfSearchResult`, `eBayHigh`, `eBayMedian`, `eBayLow`, `eBayAverage`, `TimeStamp`) VALUES ( '%s' , '%s' , '%s' , '%f' , '%f' , '%f' , '%f' , '%f' , '%s')" % (ID, cardname.replace("\'","\\'"), edition, number_of_searchResults, eBayHigh, eBayMedian, eBayLow, eBayAverage, timestamp))
        query = cur.mogrify(sql)
        xyz = cur.execute(query)
        conn.commit()
        conn.close()
    except:
        print("NO DB CONNECTION")






def main():
    rootfile = "K:\\Snapp.ai\\Final_PROJECT\\filtered_allCards.csv"
    data = exsisting_data(rootfile)
    
    for item in data:

        path = "K:\Snapp.ai\Final_PROJECT\DATA\SOLD_CARDS\English\mtg.csv"

        collected_data = extractingData(item, path)
        #print('COLLECTED DATA2',collected_data)
        
        writingSQL(collected_data)
        if collected_data != None:
            check = checkingAverage('K:\Snapp.ai\Final_PROJECT\DATA\SOLD_CARDS\English\Average.csv', collected_data)
            
            if check == False:
                writingInFile = writingAverage('K:\Snapp.ai\Final_PROJECT\DATA\SOLD_CARDS\English\Average.csv',collected_data)


if __name__ == '__main__':
    main()
