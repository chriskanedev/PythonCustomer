import csv
def save_order_to_file(store_order, order_to_save):
    if store_order == True:
        with open("resource\Entities\orderlog.csv", 'a') as order_log:
            writer = csv.writer(order_log)
            writer.writerow(order_to_save)
