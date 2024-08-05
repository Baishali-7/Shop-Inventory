
def name_phone():
    name = input("Enter your name: ")
    try_loop = True
    while try_loop == True:
        try:
            phone = int(input("Enter your phone number: "))   
            try_loop = False
        except: 
            print("Pls enter numeric values only")

    return name,phone



def disp():
    file = open("laptop.txt","r")
    ic = file.read()
    return ic

