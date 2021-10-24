import csv

def storeorder(order):
    f = open('orders.csv','a+')
    f.write(order[0]+","+order[1]+'\n')
    f.close()
