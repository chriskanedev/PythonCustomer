from src.DataSource import order_number_stub, order_number_gen

def order_number_adapt():
    testing = True
    if testing == True:
        print("in testing mode")
        order_number = order_number_stub.order_number_generator()
        return order_number
    else:
        order_number = order_number_gen.order_number_generator()
        return order_number
