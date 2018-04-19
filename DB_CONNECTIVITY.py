import pymysql

try:
    conn = pymysql.connect(host = 'snapcardster.com', port = 3306, user = 'ebay', passwd = 'ebay', db = 'ebay')
    cur = conn.cursor()
    print("CONNECTION, SUCCESSFUL")
    #conn.commit()
    conn.close()
except:
    print("ERROR, NO CONNECTION")
