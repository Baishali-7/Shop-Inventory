
# This function creates a dictionary
def di():
    file = open("laptop.txt","r")
    dictionary = {}
    lapt_id = 1

    for line in file:
        line = line.replace("\n","")
        dictionary[lapt_id]=line.split(",")
        lapt_id += 1
    return dictionary


def check_id():
    dictionary= di()

    id_valid = int(input("Please provide the ID of the laptop you want to buy "))
    while id_valid <= 0 or id_valid >len(dictionary):
                    print("Please provide a valid laptop ID\n")
                    id_valid = int(input("Please provide the ID of the laptop you want to buy"))  
    return id_valid      

def check_quantiity():
    
        
    quantity = int(input("Enter the quantity of the laptop you want to buy: "))
    while quantity <= 0:
        print("Quantity is not available please try again")
        quantity = int(input("Enter the quantity of the laptop you want to buy: "))
    return quantity

def update(id_valid,quantity):
        #UPDATE THE TEXT FILE
        dictionary = di()
        dictionary[id_valid][3] = int(dictionary[id_valid][3]) - int(quantity)
        file = open('laptop.txt','w')
        

        for values in dictionary.values():
                file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
                file.write("\n")
        file.close()


def show_bill(dictionary_user,name,phone):     
                                  
                    print("S.N \t Name \t\t Brand\t \tquantity   Price    Processor    graphics")
                    a = 1
                    file = open('laptop.txt','r')
                    for line in file:
                            print(a,"\t"+line.replace(",","\t"))
                            a+=1
                    file.close()
                    print("\n\n\n######################################################################\n")
                    print("\t\t\t\tBILL\n")     
                    print("#############################################################################\n")
                    print("\t \t \t B laptop shop\n")
                    print("\t \t \t Kirtipur,Nepal\n")
                    print("##############################################################################")
                    print("\nName of customer: "+str(name)+"\n")
                    print("Phone number of customer: "+str(phone)+"\n")
                    print("\n")
                    print("###############################################################################")
                    print("\n\nProduct name\t quantity\t Unit Price\t net amount\t Total\n")
                    
                    for i in dictionary_user.values():
                            print(str(i[0])+"\t\t"+str(i[1])+"\t\t"+str(i[2])+"\t\t"+str(i[3])+"\t\t"+str(i[4]))
                       




                
                    
                    
def sell_check_id():
    dictionary= di()

    id_valid = int(input("Please provide the ID of the laptop you want to sell "))
    while id_valid <= 0 or id_valid >len(dictionary):
                    print("Please provide a valid laptop ID\n")
                    id_valid = int(input("Please provide the ID of the laptop you want to sell"))  
    return id_valid 

def sell_check_quantity():
    quantity = int(input("Enter the quantity of the laptop you want to sell: "))
                    #VALID QUANTITY
    
    while quantity <= 0:
        print("Quantity is not available please try again")
        quantity = int(input("Enter the quantity of the laptop you want to sell: "))
    return quantity

def sell_update(id_valid,quantity):
        #UPDATE THE TEXT FILE
        dictionary = di()
        dictionary[id_valid][3] = int(dictionary[id_valid][3]) + int(quantity)
        file = open('laptop.txt','w')

        for values in dictionary.values():
                file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
                file.write("\n")
        file.close()



                    
                        


                        

                    





