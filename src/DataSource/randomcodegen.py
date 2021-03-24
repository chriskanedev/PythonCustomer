import random

def numgen(): #gets a random digit
   number = random.randint(0,9)
   return str(number)

def ordercode():#makes a random 6 digit number
   ordernum = numgen() + numgen() + numgen() + numgen() + numgen() + numgen()
   return ordernum

def order_number_generator():
   with open("resource\Entities\ordernum.txt") as order_number_file:
       order_number = [line.rstrip() for line in order_number_file]
       order_number_file.close
   newcode = ordercode()
   number_in_use = True

   while number_in_use == True:
      if newcode in order_number:
         newcode = ordercode()
      else:
         inuse = False
         order_number_file = open("resource\Entities\ordernum.txt", "a")
         order_number_file.write("\n"+ newcode)
         order_number_file.close
         return newcode

