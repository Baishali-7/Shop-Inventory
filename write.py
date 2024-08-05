def print_the_bill(dictionary_user,name,phone):
        fn =  str(phone)+ "_" + str(name) + ".txt"
                    
        with open(fn,'w') as FileBuy:
                        FileBuy.write("\n\n\n----------------------------------------------------------------------------------\n")
                        FileBuy.write("\t\t\t\tInvoice\n")
                        FileBuy.write("----------------------------------------------------------------------------------\n")
                        FileBuy.write("\t \t \tB  laptop shop \n")
                        FileBuy.write("\t \t \t Kirtipur,Nepal\n")
                        FileBuy.write("----------------------------------------------------------------------------------\n\n")
                        FileBuy.write("\nName of customer: "+str(name)+"\n")
                        FileBuy.write("Phone number of customer: "+str(phone)+"\n")
                        FileBuy.write("\n")
                        FileBuy.write("----------------------------------------------------------------------------------\n")
                        
                        FileBuy.write("----------------------------------------------------------------------------------\n")
                        FileBuy.write("\n\nProduct name\t  quantity\t Unit Price\t\tnet amount\t      Total\n")
                        for i in dictionary_user.values():
                                FileBuy.write(str(i[0])+"\t\t"+str(i[1])+"\t\t"+str(i[2])+"\t\t"+str(i[3])+"\t\t"+str(i[4])+"\n")
