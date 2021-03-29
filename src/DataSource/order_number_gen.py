import random

def order_code():
   order_num = str(random.randint(1000000,1999999))
   order_num = order_num[1:]
   return order_num

def order_number_generator():
   with open("resource\Entities\ordernum.txt") as order_number_file:
       order_number = [line.rstrip() for line in order_number_file]
       order_number_file.close
   new_code = order_code()
   number_in_use = True

   while number_in_use == True:
      if new_code in order_number:
         new_code = order_code()
      else:
         number_in_use = False
         order_number_file = open("resource\Entities\ordernum.txt", "a")
         order_number_file.write("\n"+ new_code)
         order_number_file.close
         return new_code

