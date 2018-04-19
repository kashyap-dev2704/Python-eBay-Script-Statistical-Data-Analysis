import pandas
import csv


'''
csvFileWithEd='K:\Snapp.ai\Final_PROJECT\DATA\Karstern\Demo.csv'
colnames = ['englishName', 'name', 'id']
df = pandas.read_csv(csvFileWithEd, names=colnames)
filtered = df.drop_duplicates(subset='id', keep='last')
listOfAllCardNames = list(set(filtered.englishName.tolist()))
filtered.to_csv('filtered_allCards.csv', index = False)
'''



def getWrongSearchWords(cardNameYouSearch, listOfAllCardNames):
    res = []
    splitted = cardNameYouSearch.split(" ")
    for cardName in listOfAllCardNames:
        if cardName != cardNameYouSearch and cardNameYouSearch in cardName:
            word = cardName.split(" ")
            withoutSandEmpty = [e for e in word if e != "'s" and e != "" and e not in splitted and (cardNameYouSearch+",") != e]
            res.extend(withoutSandEmpty)
    return list(set(res))

def getListOfPerfectKey(filePath):
    #csvFileWithEd=filePath
    colnames = ['englishName', 'name', 'id']
    df = pandas.read_csv(filePath, names=colnames)
    filtered = df.drop_duplicates(subset='id', keep='last')
    listOfAllCardNames = list(set(filtered.englishName.tolist()))
    filtered.to_csv('filtered_allCards.csv', index = False)
    empty_list = []
    listOfKey = {}
    with open ('filtered_allCards.csv', 'r') as collectdata:
        collectdata.readline()
        csv_reader = csv.reader(collectdata, delimiter = ',')

        for csvRow in csv_reader:
            card = csvRow[0]
            ed = csvRow[1]
            iD = csvRow[2]
            words = getWrongSearchWords(card, listOfAllCardNames)
            word = ["-" + item for item in words]
            wor = (' '.join(word))
            wor = wor.replace("(", "").replace(")", "").replace("/", "")
            print(wor)
            if len(words) != 0:
                CardName = card+ " " + wor
            else:
                CardName = card 

            final_key_dict = {'prefix':'mtg', 'cardname': card, 'edition': ed, 'ID':iD, 'cardname_for_key':CardName, 'iD':iD}
            empty_list.append (final_key_dict)
            #key = "mtg " + CardName
            #listOfKey.append(key)
    return empty_list

#x = getListOfPerfectKey('K:\Snapp.ai\Final_PROJECT\DATA\Karstern\Demo.csv')



