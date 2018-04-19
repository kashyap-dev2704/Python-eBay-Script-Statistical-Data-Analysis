import time

t = time.localtime()
timestamp = time.strftime('%d-%b-%Y@%H:%M', t)
print(timestamp)
