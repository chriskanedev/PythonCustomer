from src.DataSource.ordertofile import save_order_to_file
from src.DataSource.randomcodegen import order_number_generator
#import csv

def CreateReceipt(menu,quantity):

    order_store = True
    save_order = []

    order_number = order_number_generator()
    item_quantity = list(quantity.values())
    print(item_quantity)
    item_selected = list(quantity.keys())
    print(item_selected)
    item_price = list(menu.values())
    print(item_price)
    order_total = "£total"
    index = 0


    print(order_number)
    save_order.append("Order Number: #" + order_number)
    for quantity in item_quantity:
       if quantity == 0:
        index += 1
        continue
       print(str(item_quantity[index]) + " " + item_selected[index] + ": £" + str(item_price[index]) + "0")
       save_order.append(item_quantity)
       save_order.append(str(item_selected[index]))
       save_order.append("£"+str(item_price[index]))
       index += 1
    print("\nTOTAL: £" + order_total)
    save_order.append(order_total)
    save_order_to_file(order_store,save_order)

    #if order_store == True:
      #  with open("resource\Entities\orderlog.csv", 'a') as orderlog:
      #      order_writer = csv.writer(orderlog)
      #      order_writer.writerow(save_order)
