import csv

def storeorder(order):
    with open('orders.csv', 'w', newline='\n') as csvfile:
        fieldnames = ['Serial No.', 'FoodName','DrinkName']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=',')
        writer.writeheader()
        writer.writerow({'Serial No.': order[0], 'FoodName': order[1],'DrinkName' : order[2]})
        
