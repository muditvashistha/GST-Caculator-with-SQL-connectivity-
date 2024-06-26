global_list=[]
#CREDITS:- TEAM DESCRIPTION AND WORK DISTRIBUTION"
def creditshow():
    print("\n")
    print("*************************************************")
    
    print("Team Member's Name","            ","Field of Work")
    
    print("*************************************************")
    print("\n")
   
    print("Mudit Vashistha","            "," Set up and Coding")
    
          
    print("Suvosi Baneerjee","            ","Ideation and Documentation")

import mysql.connector
x=mysql.connector.connect(host="localhost",user="root",passwd="")
y=x.cursor()
y.execute("CREATE DATABASE abc")
y.execute("CREATE TABLE RECORD(TYPE VARCHAR(20),PRODUCT VARCHAR(20), FINALAMOUNT INTEGER)")

def writedata(types,name,amounts):
    y.execute("INSERT INTO RECORD VALUES(types,name,amounts)")
    x.commit()
    
   

#Making the functions for GST calculation

    #CGST CACLULATOR
def cgst(amount,perc):
    
    
    leest=[]
    prod=input("Mention the name of the product")
    print("\n")
    amt=amount*perc/100
    final=amount+amt
    leest.append("CGST")
    leest.append(prod)
    leest.append(final)
    writedata("CGST",prod,final)
    global_list.append(leest)
    
    
    
    
    print("Your CGST amount is", amt)
    print("\n")
    print("Your total amount of the product with CGST included is","₹", final)
    print("\n")


    #SGST CALCULATOR
def sgst(amount,perc):
    
    leest=[]
    prod=input("Mention the name of the product")
    print("\n")

    amt=amount*perc/100
    final=amount+amt
    leest.append("SGST")
    leest.append(prod)
    leest.append(final)
    writedata("SGST",prod,final)
    global_list.append(leest)
    
    
    
    
    print("Your SGST amount is", amt)
    print("\n")
    print("Your total amount of the product with SGST included is","₹", final)
    print("\n")


    #IGST CALCULATOR
def igst(inter,intra,perc,amount):
    
    leest=[]
    prod=input("Mention the name of the product")
    print("\n")
    inter_IGST= inter*perc/100
    intra_IGST= intra*perc/100
    total_IGST= inter_IGST+intra_IGST
    leest.append("IGST")
    leest.append(prod)
    
    

    print("Your Integrated GST amount is","₹", total_IGST)
    print("\n")
    print("Your final amount inclusive of IGST is","₹",amount+total_IGST)
    print("\n")
    leest.append(amount+total_IGST)
    writedata("IGST",prod,amount+total_IGST)
    global_list.append(leest)
    
    print("\n")

#STORING RECORDS IN A LIST
def rec():
    print("*************************************")
    print("OPERATION    |  PRODUCT    |     PRICE")
    print("*************************************")
    for i in global_list:
        print("\n")
        for j in i:
            print(j,end="           ")
            
            
       
    
    


#KNOW MORE ABOUT HOW GST WORKS
def know():
    print("What is GST?","\n")
    print("GST is known as the Goods and Services Tax. It is an indirect tax which has replaced many indirect taxes in India such as the excise duty, VAT, services tax, etc. The Goods and Service Tax Act was passed in the Parliament on 29th March 2017 and came into effect on 1st July 2017.")
    print("\n")
    print("What are the different types of GST?","\n")
    print("The different types of GST are CGST(central goods and services tax), SGST(state goods and services taxes), IGST(Integrated goods and services tax)","\n")
    print("How does GST work?","\n")
    print("The goods and services tax (GST) is an indirect federal sales tax that is applied to the cost of certain goods and services","\n")
    print("Do you want to learn more?")
    
    while 1:
        tell=input("Y/N")
        
        if tell=="y" or tell=="Y":
            import webbrowser
            webbrowser.open('http://www.gstcouncil.gov.in/about-gst', new=2)
            break
        elif tell=="n" or tell=="N":
            print("Sure!")
            break
        else:
            print("Invalid choice, please re-enter your choice by simply pressing 'y' for yes and 'n' for no")
            continue
            

#CURRENCY CONVERTER FUNCTION
    #RUPEE TO US DOLLAR
def rtd():
    x=int(input("Mention the amount in INR"))
    y=x/74
    print("Amount converted to USD is","$",y)
    print("\n")

 
    #DOLLAR TO RUPEE
def dtr():
    x=int(input("Enter the amount in USD"))
    y=x*74
    print("Amount converted to Rupee is","₹",y)
    print("\n")


    #USD TO Euro
def dte():
    x=int(input("Enter the amount in USD"))
    y=x*0.84
    print("Amount converted to Euro is",y,"Euros")
    print("\n")


    #Euro to USD
def etd():
    x=int(input("Enter the amount in Euro"))
    y=x/0.84
    print("Amount converted to USD is","$",y)
    print("\n")


    #Rupee to Euro
def rte():
    x=int(input("Enter the amount in INR"))
    y=x*0.011
    print("Amount converted to Euro is",y,"Euro")
    print("\n")



    #Euro to Rupee
def etr():
    x=int(input("Enter the amount in Euro"))
    y=x/0.011
    print("AAmount converted to INR is","₹",y)
    print("\n")





def getcgst():

    
    amount=int(input("Mention the price of the product"))
    print("\n")
    perc=int(input("Mention the gst percent levied on the product among 5%,12%,18%,28%"))
    print("\n")
    cgst(amount,perc)


def getsgst():
    
    amount=int(input("Mention the price of the product"))
    print("\n")
    perc=int(input("Mention the gst percent levied on the product among 5%,12%,18%,28%"))
    print("\n")
    sgst(amount,perc)

def getigst():
    amount=int(input("Mention the price of the product"))
    print("\n")
    inter=int(input("Enter the inter state value of the transaction"))
    print("\n")
    intra=int(input("Enter the intra state value of the transaction"))
    print("\n")
    
    perc=int(input("Mention the gst percent levied on the product among 5%,12%,18%,28%"))
    print("\n")
    igst(inter,intra,perc,amount)





    
    



####MENU CREATION####
from tkinter import *


   
root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="About GST", menu=filemenu)
filemenu.add_command(label="Info",command=know)




editmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Calculator", menu=editmenu)
editmenu.add_command(label="CGST", command=getcgst)
editmenu.add_command(label="SGST", command=getsgst)
editmenu.add_command(label="IGST", command=getigst)




helpmenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Converter", menu=helpmenu)
helpmenu.add_command(label="RS TO USD", command=rtd)
helpmenu.add_command(label="USD TO RS", command=dtr)
helpmenu.add_command(label="USD TO EURO", command=dte)
helpmenu.add_command(label="EURO TO USD", command=etd)
helpmenu.add_command(label="RS TO EURO", command=rte)
helpmenu.add_command(label="EURO TO RS", command=etr)

recordshow= Menu(menubar, tearoff=0)
menubar.add_cascade(label="Current Records",menu=recordshow)
recordshow.add_command(label="Show records",command=rec)

cred=Menu(menubar, tearoff=0)
menubar.add_cascade(label="Credits",menu=cred)
cred.add_command(label="Show Credits",command=creditshow)


                 
root.config(menu=menubar)
root.mainloop()















