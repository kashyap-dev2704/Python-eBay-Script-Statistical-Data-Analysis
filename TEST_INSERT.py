import pymysql


conn = pymysql.connect(host = 'snapcardster.com', port = 3306, user = 'ebay', passwd = 'ebay', db = 'ebay')    
cur = conn.cursor()
sql = ("INSERT INTO `ebay`.`KASHYAP_TABLE` (`Id`, `NameOfCard`, `Edition`, `NoOfSearchResult`, `eBayHigh`, `eBayMedian`, `eBayLow`, `eBayAverage`, `TimeStamp`) VALUES ('11230', 'Air Elemental', 'Alpha', '2.4', '15.20', '45.20', '12.01', '85.32', '12.02.2013')");
print(sql)
cur.execute(sql)
conn.commit()
conn.close()







