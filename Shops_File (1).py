#Creating databases and tables -
          
def connect_SY(Password):                                                              
    import mysql.connector as connector
    
    global con
    con = connector.connect(
            host='localhost',
            user='root',
            passwd=Password)

    global cursor   
    cursor=con.cursor()

    try:
        cursor.execute('Create database MALL_MANAGEMENT')
        cursor.execute('Use MALL_MANAGEMENT')
        query='Create table Shops(Shop_Code char(4) Primary key Not Null,\
Shop_Name varchar(50),\
Goods_Sold_Type varchar(30),\
Monthly_Rent integer,\
Monthly_Stock_Status varchar(30),\
Monthly_Customer_Count integer,\
Monthly_Profit_loss float,\
Rent_Status char(6))'
        cursor.execute(query)
        con.commit()
        
    except:
        print()
        print("Database already exists.")
        connect_SN(Password)
            

def connect_SN(Password):
    import mysql.connector as connector
    
    global con
    con = connector.connect(
            host='localhost',
            user='root',
            passwd=Password,
            database='mall_management')

    global cursor   
    cursor=con.cursor()
    

#Creating different functions for the Shops database system - 
#----------------------------------------------------------------------------------------------------------------------- 
#Function_1
    
def Add_Shop():
    ShopCode=input('Enter Shop Code(4 characters) - ')
    ShopName=input('Enter Shop Name - ')
    GoodsType=input('Enter the type of goods sold by the shop - ')
    Rent=int(input('Enter Monthly Rent - '))
    Profit_loss=int(input('Enter Profit/Loss - '))
    Customer=float(input('Enter Monthly Customer Count - '))
    query="insert into Shops(Shop_Code, Shop_Name, Goods_Sold_Type, Monthly_Rent, Monthly_Profit_Loss, Monthly_Customer_Count)\
values ('{}','{}','{}',{},{},{})".format(ShopCode,ShopName,GoodsType,Rent,Profit_loss,Customer)
    cursor.execute(query)
    con.commit()
    print()
    print('Shop added successfully.')
    
#-----------------------------------------------------------------------------------------------------------------------
#Function_2
    
def Search_Shop():
    ch3='y'
    while ch3=='y' or ch3=='Y':
        print()
        for i in range(172):
            print('-',end='')
        print()
        print('*****************'.center(172))
        print('SEARCHING SHOPS'.center(172))
        print('*****************'.center(172))
        print()
        print('  1.Update Data.'.center(172))
        print('2.View Data.'.center(172))
        print('            3.Return to SHOPS MENU.'.center(172))
        print('          4.Return to MAIN MENU.'.center(172))
        for i in range(172):
            print('-',end='')
        print()
        try:
            choice3=int(input('Please enter the serial number of the function you wish to perform - '))
            print()
            if choice3==1:
                 Update_Data()
            elif choice3==2:
                 View_Data()
            elif choice3==3:
                 import Menu
                 Menu.Shops()
            elif choice3==4:
                 import Menu
                 Menu.MainMenu()
        except:
            print('Please choose a valid option.')
        print()    
        ch2=input('Do you wish to perform any other operation in the search section (y/n) - ',)
        print()
        if ch2=='n' or ch2=='N':
            break
    
    

def Update_Data():
    ch4='y'
    while ch4=='y' or ch4=='Y':
        print()
        for i in range(172):
            print('-',end='')
        print()
        print('*****************'.center(172))
        print('UPDATING DATA'.center(172))
        print('*****************'.center(172))
        print()
        print('1.Change Shop Code.'.center(172))
        print('2.Change Shop Name.'.center(172))
        print('        3.Change Type of Goods sold.'.center(172))
        print('  4.Change Monthly Rent.'.center(172))
        print('             5.Change Monthly Stock Supplies.'.center(172))
        print('             6.Change Monthly Customer Count.'.center(172))
        print('          7.Change Monthly Profit/Loss.'.center(172))
        print('  8.Change Rent Status.'.center(172))
        print('        9.Return to SEARCHING SHOPS.'.center(172))
        for i in range(172):
            print('-',end='')
        try:    
            print()
            choice4=int(input('Please enter the serial number of the function you wish to perform - '))
            print()
            if choice4==1:
                 Change_Code()
            elif choice4==2:
                 Change_Name()   
            elif choice4==3:
                 Change_Goods()
            elif choice4==4:
                 Change_Rent()
            elif choice4==5:
                 Change_Stocks()
            elif choice4==6:
                 Change_Customer()
            elif choice4==7:
                 Change_P_L()
            elif choice4==8:
                 Change_Status()
            elif choice4==9:
                 Search_Shop()
        except:
            print('Please choose a valid option.')
        print()    
        ch2=input('Do you wish to perform any other operation in the update section (y/n) - ',)
        print()
        if ch2=='n' or ch2=='N':
            break
    

def Change_Code():
    OldCode=input('Enter old Shop Code - ')
    NewCode=input('Enter new Shop Code - ')
    query="Update Shops Set Shop_Code='{}' where Shop_Code='{}'".format(NewCode,OldCode)
    cursor.execute(query)
    con.commit()
    print()
    print('Data updated successfully.')

def Change_Name():
    ShopCode=input('Enter Shop Code - ')
    NewName=input('Enter New Name - ')
    query="Update Shops Set Shop_Name='{}' where Shop_Code='{}'".format(NewName,ShopCode)
    cursor.execute(query)
    con.commit()
    print()
    print('Data updated successfully.')

def Change_Goods():
    ShopCode=input('Enter Shop Code - ')
    NewType=input('Enter new type of goods to be sold - ')
    query="Update Shops Set Goods_Sold_Type = '{}' where Shop_Code='{}'".format(NewType,ShopCode)
    cursor.execute(query)
    con.commit()
    print()
    print('Data updated successfully.')

    
def Change_Rent():
    ShopCode=input('Enter Shop Code - ')
    NewRent=int(input('Enter Rent(Monthly) - '))
    query="Update Shops Set Monthly_Rent={} where Shop_Code='{}'".format(NewRent,ShopCode)
    cursor.execute(query)
    con.commit()
    print()
    print('Data updated successfully.')

def Change_Stocks():
    ShopCode=input('Enter Shop Code - ')
    Stocks=input('Enter the required units(Monthly) - ')
    query="Update Shops Set Monthly_Stock_Status = '{} units' where Shop_Code='{}'".format(Stocks,ShopCode)
    cursor.execute(query)
    con.commit()
    print()
    print('Data updated successfully.')

def Change_Customer():
    ShopCode=input('Enter Shop Code - ')
    Customer=int(input('Enter Customer Count(Monthly) - '))
    query="Update Shops Set Monthly_Customer_Count = {} where Shop_Code='{}'".format(Customer,ShopCode)
    cursor.execute(query)
    con.commit()
    print()
    print('Data updated successfully.')

def Change_P_L():
    ShopCode=input('Enter Shop Code - ')
    PL=float(input('Enter Profit/Loss(Monthly) - '))
    query="Update Shops Set Monthly_Profit_loss = {} where Shop_Code='{}'".format(PL,ShopCode)
    cursor.execute(query)
    con.commit()
    print()
    print('Data updated successfully.')

def Change_Status():
    ShopCode=input('Enter Shop Code - ')
    Status=input('Enter Status(Paid/Unpaid) - ')
    query="Update Shops Set Rent_Status = '{}' where Shop_Code='{}'".format(Status,ShopCode)
    cursor.execute(query)
    con.commit()
    print()
    print('Data updated successfully.')


def View_Data():
    ShopCode=input('Enter Shop Code - ')
    print()
    print('REQUIRED DATA'.center(172))
    print('----------------------------'.center(172))
    print('------------'.center(172))
    query="Select * from Shops where Shop_Code = '{}'".format(ShopCode)
    cursor.execute(query)
    list1=['SHOP CODE','SHOP NAME','GOODS SOLD','MONTHLY RENT','MONTHLY STOCK STATUS','MONTHLY CUSTOMER COUNT','MONTHLY PROFIT/LOSS','RENT STATUS']
    for i in cursor:
        print()
        print()
        for j in range(0,8):
            print()
            str1=(list1[j]).center(172)
            print(str1)
            str2=str(i[j])
            print(str2.center(172))

            
#-----------------------------------------------------------------------------------------------------------------------
#Function_3
    
def Delete_Shop():
    ShopCode=input('Enter the Shop Code whose data you wish to delete - ')
    query="Delete from Shops where Shop_Code = '{}'".format(ShopCode)
    cursor.execute(query)
    con.commit()
    print()
    print('Data deleted successfully.')

            
#-----------------------------------------------------------------------------------------------------------------------
#Function_4

def P_L_bar():
    cursor.execute("select * from shops")
    data=cursor.fetchall()
    list_Shop=[]
    list_P_L=[]
    for i in data:
        ele1=i[0]
        list_Shop.append(ele1)
        ele2=i[6]
        list_P_L.append(ele2)
    import matplotlib.pyplot as plt
    plt.bar(list_Shop,list_P_L)
    plt.xlabel('Shop Codes')
    plt.ylabel('Profit/Loss')
    plt.title('Bar Graph')
    plt.show()
   
#-----------------------------------------------------------------------------------------------------------------------
#Function_5

def Pie_Chart():
    cursor.execute("select * from shops")
    data=cursor.fetchall()
    list_Shop=[]
    list_Count=[]
    for i in data:
        ele1=i[0]
        list_Shop.append(ele1)
        ele2=i[5]
        list_Count.append(ele2)
    import matplotlib.pyplot as plt
    plt.pie(list_Count,labels=list_Shop,autopct="%.1f%%")
    plt.title("Pie Chart for Customer Count")
    plt.show()
        
    
    
    
    
    
