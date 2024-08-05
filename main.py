     
import read
from read import name_phone,disp
from  operations import di, check_id,check_quantiity,update,show_bill,sell_check_id,sell_check_quantity,sell_update
from write import print_the_bill


print("\n")
print("##################################################################")
print("\t \t B laptop shop")
print("##################################################################")
print("\t \t kirtipur,Nepal")
print("##################################################################")

print("\n")

print("Name \t       Brand\t  Price  Quantity   Processor   Graphics")
file = open('laptop.txt','r')
lines = file.read()
print(lines)
file.close()


loop = True

while loop == True:
    print("Press 1 to buy")
    print("Press 2 to sell")
    print("Press 3 to exit")
    try_loop = True
    while try_loop == True:
        try:    
            user_input = int(input("Enter your preferred option: "))
            try_loop= False
        except:
            print("ERROR ")

    if user_input == 1:
        name, phone = name_phone()
        dictionary = di()
        
        dictionary_user = {}
        more = True
        while more == True:
            print(disp())
            id_valid = check_id()
            quantity = check_quantiity()

            update(id_valid,quantity)
            

            product = dictionary[id_valid][0]
            one = dictionary[id_valid][2]
            price = dictionary[id_valid][2].replace("$","")
            quan = int(quantity)
            tot = int(price)*int(quan)
            
        
            
            dictionary_user[id_valid] = (product,quan,one,price,tot)

        

            ask_more = input("Do you want to buy more laptops?(y/n)").lower()
            if ask_more == "y":
                more = True
            else:
                print("Price with added vat\n")
                total = 0
                grand = 0
                
                vat = total*(0.13)
                grand = total+vat
                show_bill(dictionary_user,name,phone)
                print_the_bill(dictionary_user,name,phone)
                more = False

        

            
                

    elif user_input == 2:
        name, phone = name_phone()
        dictionary = di()
        
        dictionary_user = {}
        more = True
        while more == True:
            print(disp())
            id_valid = sell_check_id()
            quantity =  sell_check_quantity()

            sell_update(id_valid,quantity)

            product = dictionary[id_valid][0]
            one = dictionary[id_valid][2]
            price = dictionary[id_valid][2].replace("$","")
            quan = int(quantity)
            tot = int(price)*int(quan)
            
        
            
            dictionary_user[id_valid] = (product,quan,one,price,tot)

        

            ask_more = input("Do you want to buy more laptops?(y/n)").lower()
            if ask_more == "y":
                more = True
            else:
                print("Price with added vat\n")
                total = 0
                grand = 0
                shipping = 0
                
                shipping = total+100
                grand = total+shipping
                show_bill(dictionary_user,name,phone)
                print_the_bill(dictionary_user,name,phone)
                more = False


        pass
        
    elif user_input == 3:
        print("Thank you for using our program")
        loop = False
    

