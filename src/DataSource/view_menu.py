def view_menu():
    with open("resource\Entities\menu.txt") as menu_file:
        items_menu = [line.rstrip() for line in menu_file]
        menu_file.close
    for items in items_menu:
        readable_item = items.split("^")
        print(readable_item[0] + ",  £" + readable_item[1])
