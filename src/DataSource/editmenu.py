def addmenu(name_item, price_pound = 0, price_pence = 0):
    try:
        price_pound = int(price_pound)
    except ValueError:
        print("a number is required here")
        return
    try:
        price_pence = int(price_pence)
    except ValueError:
        print("a number is required here")
        return
    if len(str(price_pence)) == 1:
        price_pence = "0" + str(price_pence)
    newitem =  name_item + "^" + str(price_pound) + "." + str(price_pence)
    menu_file = open("resource\Entities\menu.txt", "a")
    menu_file.write("\n"+ newitem)
    menu_file.close

def addhelp():
    print('To add an item to the menu type addmenu("name of item", pounds, pence) \n'
          'an example of this would be additem(donut,1,50) to ad a donut at £1.50')
