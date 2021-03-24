import csv

store_order = True
order_to_save = []

#import from basket
order_number = "000000"
ordered_items = ["item 1", "item 2", "item 3"]
ordered_price = ["1.00", "1.00", "1.00"]
order_total = "£total"
index_traker =0

order_to_save.append("#" + order_number)
for item in ordered_items:
    order_to_save.append(str(ordered_items[index_traker]))
    order_to_save.append("£"+ordered_price[index_traker])
    index_traker += 1
order_to_save.append(order_total)
if store_order == True:
    with open("resource\Entities\orderlog.csv", 'a') as orderlog:
        writer = csv.writer(orderlog)
        writer.writerow(order_to_save)
