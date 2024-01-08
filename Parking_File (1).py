#Creating databases and tables -

def connect_PY(Password):                                                             
    import mysql.connector as connector
    
    global con
    con = connector.connect(
            host='localhost',
            user='root',
            passwd=Password)

    global cursor   
    cursor=con.cursor()

    try:
        cursor.execute('Use MALL_MANAGEMENT')
        query='Create table Parking(License_Number char(16) Primary key Not Null,\
Car_Model varchar(30),\
Entry_time char(8),\
Exit_time char(8),\
Date char(10),\
TotalRevenue_30perhr integer)'
        cursor.execute(query)
        con.commit()
        
    except:
        connect_PN(Password)
            

def connect_PN(Password): 
    import mysql.connector as connector
    
    global con
    con = connector.connect(
            host='localhost',
            user='root',
            passwd=Password,
            database='mall_management')

    global cursor   
    cursor=con.cursor()

#Creating different functions for the Parking database system -    
#----------------------------------------------------------------
#Function 1 -
    
def Enter_Record():
    print()
    Number=input('Enter vehicle\'s License Number(16 Character long) - ')
    Model=input('Enter vehicle\'s Model - ')
    NTime=input('Enter Entry Time - ')
    Date=input('Enter Date - ')
    query="insert into Parking(License_Number,Car_Model,Entry_Time,Date) values('{}','{}','{}','{}')".format(Number,Model,NTime,Date)
    cursor.execute(query)
    con.commit()
    print()
    print('Data entered succcessfuly.')

#----------------------------------------------------------------
#Function 2 -
    
def See_Records():
    print()
    print('-------------'.center(172))
    print('RECORDS'.center(172))
    print('-------------'.center(172))
    print()
    print('Format - [License Number, Car Model, Entry Time, Exit Time, Date, Revenue Generated]'.center(172))
    print('-----------------------------------------------------------------------------------------------'.center(172))
    print('--------------------------------------------'.center(172))
    print()
    print()
    query="select * from Parking"
    cursor.execute(query)
    data=cursor.fetchall()
    for i in data:
        str1=str(i)
        print(str1.center(172))
        print()
        
#----------------------------------------------------------------
#Function 3 -
def Enter_Exit():
    print()
    print('-------------------------------------------------------------'.center(172))
    print('Use a 24hr clock system.'.center(172))
    print('Format for Writing time - hours:minutes:seconds'.center(172))
    print('Eg - 12:30:45'.center(172))
    print('-------------------------------------------------------------'.center(172))
    print()
    Number=input('Enter License Number - ')
    Time_Exit=input('Enter time of exit - ')
    query="Update Parking Set Exit_time = '{}' where License_Number = '{}'".format(Time_Exit,Number)
    cursor.execute(query)
    con.commit()
    print()
    print('Data entered successfully.')

    

    query="Select Entry_time from parking where License_Number = '{}'".format(Number)
    cursor.execute(query)
    data=cursor.fetchone()
    Time_Entry=data[0]


    
    if len(Time_Entry)==7:
        Time_1=int(Time_Entry[0])
    else:
        Time_1=int(Time_Entry[0:2])

    if len(Time_Exit)==7:
        Time_2=int(Time_Exit[0])
    else:
        Time_2=int(Time_Exit[0:2])
        
    
    diff = Time_2 - Time_1
    Revenue = diff*30
    query="Update parking Set TotalRevenue_30perhr = {} where License_Number = '{}'".format(Revenue,Number)
    cursor.execute(query)
    con.commit()
    
  
#----------------------------------------------------------------
#Function 4 -
    
def See_Revenue():
    print()
    print('-------------'.center(172))
    print('Total Revenue Generated'.center(172))
    print('-------------'.center(172))
    query="select sum(TotalRevenue_30perhr) from parking"
    cursor.execute(query)
    data=cursor.fetchone()[0]
    data=str(data)
    print()
    print(data.center(172))
    
