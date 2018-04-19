import pandas
import csv

csvFileWithEd='K:\Snapp.ai\Final_PROJECT\DATA\Karstern\Demo.csv'
colnames = ['englishName', 'name', 'id']
df = pandas.read_csv(csvFileWithEd, names=colnames)
#print(df)
filtered = df.drop_duplicates(subset='id', keep='last')
#print(filtered)
listOfAllCardNames = list(set(filtered.englishName.tolist()))
#print(listOfAllCardNames)
filtered.to_csv('filtered_allCards.csv', index = False)

def getWrongSearchWords(cardNameYouSearch, listOfAllCardNames):
    res = []
    splitted = cardNameYouSearch.split(" ")
    for cardName in listOfAllCardNames:
        if cardName != cardNameYouSearch and cardNameYouSearch in cardName:
            word = cardName.split(" ")
            withoutSandEmpty = [e for e in word if e != "'s" and e != "" and e not in splitted and (cardNameYouSearch+",") != e]
            res.extend(withoutSandEmpty)
    return list(set(res))

def getListOfPerfectKey():
    listOfKey = []
    with open ('filtered_allCards.csv', 'r') as collectdata:
        collectdata.readline()
        csv_reader = csv.reader(collectdata, delimiter = ',')

        for csvRow in csv_reader:
            #print(csvRow)
            card = csvRow[0]
            ed = csvRow[1]
            iD = csvRow[2]
            words = getWrongSearchWords(card, listOfAllCardNames)
            word = ["-" + item for item in words]
            wor = (' '.join(word))
            wor = wor.replace("(", "").replace(")", "").replace("/", "")
            if len(words) != 0:
                CardName = card+ " " + ed + " " + wor
            else:
                CardName = card + " " +ed

            key = "mtg " + CardName
            #print(key)
            listOfKey.append(key)
    return listOfKey

x = getListOfPerfectKey()
#print(x)

#input("Please, Press Enter to exit")
